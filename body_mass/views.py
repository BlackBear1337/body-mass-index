from django.shortcuts import render

def index(request):
    if request.method == 'GET':
        m = float(request.GET.get('m', '1'))
        h = float(request.GET.get('h', '1'))
        h = h/100
        i = float(m / (h * h))
        # index_list = {"body_index": "Индекс тела равен: ", "mass_defect": "выраженный дефицит массы тела",
        #               "underweight": "недостаточная масса тела", "norm": "норма",
        #               "overweight": "избыточная масса тела", "obesity_one_degree": "ожирение 1 степени",
        #               "obesity_two_degree": "ожирение 2 степени", "obesity_three_degree": "ожирение 3 степени"}
        body_index = "Индекс тела равен: "
        mass_defect = "(выраженный дефицит массы тела)"
        underweight = "(недостаточная масса тела)"
        norm = "(норма)"
        overweight = "(избыточная масса тела)"
        obesity_one_degree = "(ожирение 1 степени)"
        obesity_two_degree = "(ожирение 2 степени)"
        obesity_three_degree = "(ожирение 3 степени)"


        if float(i) < 16:
            return render(request, 'index.html', {'body_index': body_index, 'mass_defect': mass_defect, 'i': i, 'method': request.method})
        elif i >= 16 and float(i) <= 18.5:
            return render(request, 'index.html', {'body_index': body_index, 'underweight': underweight, 'i': i, 'method': request.method})
        elif i >= 18.5 and float(i) <= 24.99:
            return render(request, 'index.html', {'body_index': body_index, 'norm': norm, 'i': i, 'method': request.method})
        elif i >= 25 and float(i) <= 30:
            return render(request, 'index.html', {'body_index': body_index, 'overweight': overweight, 'i': i, 'method': request.method})
        elif i >= 30 and float(i) <= 35:
            return render(request, 'index.html', {'body_index': body_index, 'obesity_one_degree': obesity_one_degree, 'i': i, 'method': request.method})
        elif i >= 35 and float(i) <= 40:
            return render(request, 'index.html', {'body_index': body_index, 'obesity_two_degree': obesity_two_degree, 'i': i, 'method': request.method})
        elif i >= 40:
            return render(request, 'index.html', {'body_index': body_index, 'obesity_three_degree': obesity_three_degree, 'i': i, 'method': request.method})