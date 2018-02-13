# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import CompanyUser, UserDateData, UserEnumData, UserNumberData
from .models import UserTextData, Company, CompanyRiskFields, CompanyRiskTypes, UserEnumOption

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyRiskFields)
admin.site.register(CompanyRiskTypes)
admin.site.register(CompanyUser)
admin.site.register(UserDateData)
admin.site.register(UserEnumData)
admin.site.register(UserEnumOption)
admin.site.register(UserNumberData)
admin.site.register(UserTextData)
