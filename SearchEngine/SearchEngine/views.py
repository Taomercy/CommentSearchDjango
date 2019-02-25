#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
import re


def SearchFunc(request):
    context = {}
    results =[]
    if request.method == "POST":
        key_char = request.POST.get('key_char', None).split(',')
        str_context = request.POST.get('str_context', None).split('\n')
        print "searching:", key_char
        print "str_context:", str_context
        for key in key_char:
            for line in str_context:
                if key in line:
                    results.append(line)
        context['search_results'] = list(set(results))

    return render(request, 'SearchEngine/SearchPage.html', context=context)
