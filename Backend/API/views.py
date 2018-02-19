# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse

from .models import *


def risk(request, company_id, risk_id):
    """

    :param request:
    :param company_id:
    :param risk_id:
    :return:
    """
    if request.method == 'GET':
        try:
            risk_type = CompanyRiskTypes.objects.get(id=risk_id)
            if risk_type.companyID.id != int(company_id):
                return JsonResponse({"error": "company has no such risk"})
        except:
            return JsonResponse({"error": "company has no such risk"})
        result = get_risk(risk_id)
        return JsonResponse({"result": result})
    if request.method == 'POST':
        new_data = json.loads(request.body)
        risk_type = CompanyRiskTypes.objects.get(id=risk_id)
        table_heads = CompanyRiskFields.objects.filter(RiskTypeID=risk_id)
        user_obj = CompanyUser(RiskTypeID=risk_type)
        user_obj.save()
        for th in table_heads:
            if th.fieldType == 'text':
                td = UserTextData(CompanyRiskFieldsID=th,
                                  companyUserID=user_obj,
                                  value=new_data[th.fieldName])
                td.save()
            elif th.fieldType == 'date':
                td = UserDateData(CompanyRiskFieldsID=th,
                                  companyUserID=user_obj,
                                  value=new_data[th.fieldName])
                td.save()
            elif th.fieldType == 'number':
                td = UserNumberData(CompanyRiskFieldsID=th,
                                    companyUserID=user_obj,
                                    value=new_data[th.fieldName])
                td.save()
            elif th.fieldType == 'enum':
                td = UserEnumData(CompanyRiskFieldsID=th,
                                  companyUserID=user_obj,
                                  value=new_data[th.fieldName])
                td.save()
        result = get_risk(risk_id)
        return JsonResponse({"result": result},status=201)


def all_risk(request, company_id):
    if request.method == 'GET':
        risks_types = CompanyRiskTypes.objects.filter(companyID=company_id)
        if not risks_types:
            return JsonResponse({"result": []})
        all_risks = []
        for risk_type in risks_types:
            obj_temp = {}
            risk_data = get_risk(risk_type.id)
            obj_temp['id'] = risk_type.id
            obj_temp['riskName'] = risk_type.riskName
            obj_temp['data'] = risk_data
            all_risks.insert(len(all_risks), obj_temp)
        return JsonResponse({"result": all_risks})


def get_risk(risk_id):
    table_heads = CompanyRiskFields.objects.filter(RiskTypeID=risk_id)
    user_obj = CompanyUser.objects.filter(RiskTypeID=risk_id)
    result = []
    # loop over each data in risk and save it on object
    for tr in user_obj:
        obj_temp = {}
        for th in table_heads:
            enum_options = []
            td = []
            if th.fieldType == 'text':
                td = UserTextData.objects.filter(CompanyRiskFieldsID=th.id,
                                                 companyUserID=tr.id)
            elif th.fieldType == 'date':
                td = UserDateData.objects.filter(CompanyRiskFieldsID=th.id,
                                                 companyUserID=tr.id)
            elif th.fieldType == 'number':
                td = UserNumberData.objects.filter(CompanyRiskFieldsID=th.id,
                                                   companyUserID=tr.id)
            elif th.fieldType == 'enum':
                td = UserEnumData.objects.filter(CompanyRiskFieldsID=th.id,
                                                 companyUserID=tr.id)
                enum_options = UserEnumOption.objects.filter(EnumID=th.id)
            if len(td) > 0:
                obj_temp[th.fieldName] = {"id": td[0].id,
                                          "type": th.fieldType,
                                          "data": td[0].value,
                                          "options": [
                                              x.value for x in enum_options
                                          ]}
        result.insert(len(result), obj_temp)
    return result
