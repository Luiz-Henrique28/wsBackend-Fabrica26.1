from django.http import HttpResponse

def test_view(request):
    return HttpResponse("""
    <h1>App Quiz conectada com sucesso!</h1>
    """)
