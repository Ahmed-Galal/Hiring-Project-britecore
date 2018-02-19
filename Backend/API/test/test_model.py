from django.test import TestCase

from ..models import (
    Company, CompanyRiskTypes, CompanyRiskFields,
    CompanyUser, UserNumberData, UserDateData, UserTextData)


class TestCompanyModel(TestCase):
    def setUp(self):
        self.Company = Company(name="MOHY.CO")
        self.Company.save()

    def test_Company_creation(self):
        self.assertEqual(Company.objects.count(), 1)

    def test_Company_representation(self):
        self.assertEqual(self.Company.name, str(self.Company))


class TestCompanyRiskTypesModel(TestCase):
    def setUp(self):
        self.Company = Company(name="MOHY.CO")
        self.Company.save()
        self.CompanyRiskTypes = CompanyRiskTypes(
            riskName="Rain", companyID=self.Company)
        self.CompanyRiskTypes.save()

    def test_CompanyRiskTypes_creation(self):
        self.assertEqual(CompanyRiskTypes.objects.count(), 1)

    def test_CompanyRiskTypes_representation(self):
        self.assertEqual(
            self.CompanyRiskTypes.riskName, str(self.CompanyRiskTypes))


class TestCompanyRiskFieldsModel(TestCase):
    def setUp(self):
        self.Company = Company(name="MOHY.CO")
        self.Company.save()

        self.CompanyRiskTypes = CompanyRiskTypes(
            riskName="Rain", companyID=self.Company)
        self.CompanyRiskTypes.save()

        self.CompanyRiskFields = CompanyRiskFields(
            fieldName="Rain", RiskTypeID=self.CompanyRiskTypes, fieldType='text')
        self.CompanyRiskFields.save()

    def test_CompanyRiskTypes_creation(self):
        self.assertEqual(CompanyRiskFields.objects.count(), 1)

    def test_CompanyRiskTypes_representation(self):
        self.assertEqual(self.CompanyRiskFields.fieldName, str(
            self.CompanyRiskFields))


class TestCompanyUserModel(TestCase):
    def setUp(self):
        self.Company = Company(name="MOHY.CO")
        self.Company.save()

        self.CompanyRiskTypes = CompanyRiskTypes(
            riskName="Rain", companyID=self.Company)
        self.CompanyRiskTypes.save()

        self.CompanyUser = CompanyUser(RiskTypeID=self.CompanyRiskTypes)
        self.CompanyUser.save()

    def test_CompanyUser_creation(self):
        self.assertEqual(CompanyUser.objects.count(), 1)

    def test_CompanyUser_representation(self):
        self.assertEqual(self.CompanyUser.RiskTypeID, self.CompanyRiskTypes)


class TestUserDataModel(TestCase):
    def setUp(self):
        self.Company = Company(name="MOHY.CO")
        self.Company.save()

        self.CompanyRiskTypes = CompanyRiskTypes(
            riskName="Rain", companyID=self.Company)
        self.CompanyRiskTypes.save()

        self.CompanyRiskFields = CompanyRiskFields(
            fieldName="number", RiskTypeID=self.CompanyRiskTypes,
            fieldType='number')
        self.CompanyRiskFields.save()

        self.CompanyUser = CompanyUser(RiskTypeID=self.CompanyRiskTypes)
        self.CompanyUser.save()

        self.UserDateData = UserDateData(
            value='2018-9-9',
            CompanyRiskFieldsID=self.CompanyRiskFields,
            companyUserID=self.CompanyUser)
        self.UserDateData.save()
        self.UserTextData = UserTextData(
            value='testtext',
            CompanyRiskFieldsID=self.CompanyRiskFields,
            companyUserID=self.CompanyUser)
        self.UserTextData.save()
        self.UserNumberData = UserNumberData(
            value=77,
            CompanyRiskFieldsID=self.CompanyRiskFields,
            companyUserID=self.CompanyUser)
        self.UserNumberData.save()

    def test_UserDateData_creation(self):
        self.assertEqual(UserDateData.objects.count(), 1)
        self.assertEqual(UserTextData.objects.count(), 1)
        self.assertEqual(UserNumberData.objects.count(), 1)
