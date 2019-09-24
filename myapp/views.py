from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json
import timeit

@api_view(["POST"])
def fibonacci(num):
	s = 1
	s1 = 1
	try:
		start = timeit.timeit()
		n=json.loads(num.body)


		for i in range(n):
			if i == 0:
				c = s

			elif i == 1:
				c = s1

			else:
				
				c = s1 + s
				s = s1
				s1 = c
		    
		end = timeit.timeit()
		total_time = end - start
		return Response({'res':c,'time_taken':total_time})
	except Exception as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

  