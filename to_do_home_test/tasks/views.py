from django.shortcuts import render, HttpResponse

# Create your views here.


def get_home_page(request):
    "My text {} ends here".format(5)
    "My text {} ends here".format(532)
    "My text {} ends here".format(51)

    return render(request, "tasks/home.html")
