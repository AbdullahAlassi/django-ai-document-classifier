from django.shortcuts import render
from analyzer.local_llm import classify_with_ollama
from .models import Document


def upload_document(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        category = classify_with_ollama(content)

        Document.objects.create(
            title=title,
            content=content,
            predicted_category=category
        )

    docs = Document.objects.all().order_by("-created_at")

    if request.headers.get("HX-Request") == "true":
        return render(request, "_history.html", {"docs": docs})

 
    return render(request, "upload.html", {"docs": docs})