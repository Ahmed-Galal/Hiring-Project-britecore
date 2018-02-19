from django.shortcuts import reverse
from rest_framework.test import APITestCase

from ..models import (
    Company, CompanyRiskTypes, CompanyRiskFields,
    CompanyUser, UserNumberData, UserDateData, UserTextData)


class TestRiskApi(APITestCase):
    def setUp(self):
        # create risk
        self.Company = Company(name="MOHY.CO")
        self.Company.save()

        self.CompanyRiskTypes = CompanyRiskTypes(
            riskName="Rain", companyID=self.Company)
        self.CompanyRiskTypes.save()

        self.CompanyRiskFields1 = CompanyRiskFields(
            fieldName="number", RiskTypeID=self.CompanyRiskTypes,
            fieldType="number")
        self.CompanyRiskFields2 = CompanyRiskFields(
            fieldName="text", RiskTypeID=self.CompanyRiskTypes,
            fieldType="text")
        self.CompanyRiskFields3 = CompanyRiskFields(
            fieldName="date", RiskTypeID=self.CompanyRiskTypes,
            fieldType="date")

        self.CompanyRiskFields1.save()
        self.CompanyRiskFields2.save()
        self.CompanyRiskFields3.save()

        self.CompanyUser = CompanyUser(RiskTypeID=self.CompanyRiskTypes)
        self.CompanyUser.save()

        self.UserNumberData = UserNumberData(
            value=77,
            CompanyRiskFieldsID=self.CompanyRiskFields1,
            companyUserID=self.CompanyUser)

        self.UserDateData = UserDateData(
            value='2018-9-9',
            CompanyRiskFieldsID=self.CompanyRiskFields1,
            companyUserID=self.CompanyUser)

        self.UserTextData = UserTextData(
            value='mohytext',
            CompanyRiskFieldsID=self.CompanyRiskFields1,
            companyUserID=self.CompanyUser)

        self.UserNumberData.save()
        self.UserDateData.save()
        self.UserTextData.save()

    def test_risk_creation(self):
        response = self.client.post(
            reverse(
                "riskview", kwargs={
                    "company_id": self.Company.id, "risk_id": self.CompanyRiskTypes.id}
            ),
            {"number": 44, "text": "mohy", "date": "2018-9-9"}, format="json")

        # assert new movie was added
        self.assertEqual(CompanyUser.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_risk(self):
        response = self.client.get(
            reverse(
                "riskview", kwargs={
                    "company_id": self.Company.id, "risk_id": self.CompanyRiskTypes.id}
            ), format="json")
        self.assertEqual(len(response._container), 1)
        self.assertEqual(200, response.status_code)

    def test_getting_allrisk(self):
        response = self.client.get(
            reverse(
                "allriskview", kwargs={
                    "company_id": self.Company.id}
            ), format="json")
        self.assertEqual(len(response._container), 1)
        self.assertEqual(200, response.status_code)