from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdminUser
from rest_framework import status, generics
from .models import Quiz, Question, Option,UserQuizSubmission, UserAnswer
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer, QuizSubmissionSerializer,UserQuizSubmissionSerializer
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# creating quiz for admin only
class CreateQuizView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Add a question admin only
class AddQuestionView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, quiz_id):
        quiz = Quiz.objects.filter(pk=quiz_id).first()
        if not quiz:
            return Response({"error": f"Quiz with id {quiz_id} not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['quiz'] = quiz.id

        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Add options admin only
class AddOptionView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=404)

        data = request.data.copy()
        data['question'] = question.id

        serializer = OptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class QuestionDetailView(APIView):
    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=404)

        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class QuizSubmissionView(APIView):
    def post(self, request):
        serializer = QuizSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            quiz_id = serializer.validated_data['quiz']
            answers = serializer.validated_data['answers']

            try:
                quiz = Quiz.objects.get(id=quiz_id)
            except Quiz.DoesNotExist:
                return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

            score = 0
            total_questions = quiz.questions.count()

            # Create the submission object
            submission = UserQuizSubmission.objects.create(user=request.user, quiz=quiz)

            for answer in answers:
                question_id = answer.get('question')
                selected_option_id = answer.get('option')

                try:
                    question = Question.objects.get(id=question_id, quiz=quiz)
                    selected_option = Option.objects.get(id=selected_option_id, question=question)
                except (Question.DoesNotExist, Option.DoesNotExist):
                    continue  # skip invalid question/option pair

                # Save the user answer
                UserAnswer.objects.create(
                    submission=submission,
                    question=question,
                    selected_option=selected_option
                )

                if selected_option.is_correct:
                    score += 1

            submission.score = score
            submission.save()

            return Response({
                "message": "Quiz submitted successfully",
                "score": score,
                "total": total_questions
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSubmissionHistoryView(generics.ListAPIView):
    serializer_class = UserQuizSubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserQuizSubmission.objects.filter(user=self.request.user)
