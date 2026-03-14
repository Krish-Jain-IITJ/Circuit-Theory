from unittest import result

from django.shortcuts import render

import json




def home(request):
    return render(request,'index.html')
# Create your views here.

from django.http import FileResponse, Http404
import os
from django.conf import settings

def theory_pdf_view(request):
    path = os.path.join(settings.BASE_DIR, 'myapp/static/circuit_theory.pdf')
    print(path)

    try:
        return FileResponse(open(path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("Theory manual not found")
    

from django.shortcuts import render
from .solver import solve_circuit_network


def solve_circuit(request):

    if request.method == "POST":

        r = float(request.POST.get("res", 0))
        c = float(request.POST.get("cap", 0))
        l = float(request.POST.get("ind", 0))
        n = int(request.POST.get("loops", 1))

        result , A , I = solve_circuit_network(r, c, l, n)

        return render(request, "index.html", {
            "result":result,
            "matrix": A.tolist(),
            "currents": I.tolist(),
            "r": r,
            "c": c,
            "l": l,
            "n": n,
            "loops":n*n
        })

    return render(request, "index.html")

# context = {
#     "result": result,
#     "result_json": json.dumps([str(z) for z in result]),
# }