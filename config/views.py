from django.shortcuts import redirect


def handler_404(request, exception):
    return redirect("note:index")
