# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    """
        this is company table and it is supposed to be the  user
        and auth should be done here by creating more table data password
        or just extends  default django users
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class CompanyRiskTypes(models.Model):
    """
       Risktype table company can have as risk as it want

       """
    riskName = models.CharField(max_length=100)
    companyID = models.ForeignKey(Company)

    def __unicode__(self):
        return self.riskName


class CompanyRiskFields(models.Model):
    """
       to make company able to add field so we make this model
       so company can add field and it's type
       """
    fieldName = models.CharField(max_length=100)
    RiskTypeID = models.ForeignKey(CompanyRiskTypes)
    fieldType = models.CharField(max_length=100, choices=(
        ('text', 'text'), ('date', 'date'),
        ('number', 'number'), ('enum', 'enum')
    ))

    def __unicode__(self):
        return self.fieldName


class CompanyUser(models.Model):
    """
        just to make data unique so it is identifer for each row
        company user cuase it may be user data of each risk
    """
    RiskTypeID = models.ForeignKey(CompanyRiskTypes)

    def __unicode__(self):
        return "{}:{}".format(self.RiskTypeID.riskName, self.id)


class UserNumberData(models.Model):
    value = models.FloatField()
    CompanyRiskFieldsID = models.ForeignKey(CompanyRiskFields)
    companyUserID = models.ForeignKey(CompanyUser)


class UserDateData(models.Model):
    value = models.DateField()
    CompanyRiskFieldsID = models.ForeignKey(CompanyRiskFields)
    companyUserID = models.ForeignKey(CompanyUser)


class UserTextData(models.Model):
    value = models.TextField()
    CompanyRiskFieldsID = models.ForeignKey(CompanyRiskFields)
    companyUserID = models.ForeignKey(CompanyUser)


class UserEnumData(models.Model):
    value = models.TextField()
    CompanyRiskFieldsID = models.ForeignKey(CompanyRiskFields)
    companyUserID = models.ForeignKey(CompanyUser)


class UserEnumOption(models.Model):
    value = models.TextField()
    EnumID = models.ForeignKey(CompanyRiskFields)
