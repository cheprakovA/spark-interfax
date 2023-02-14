import pyarrow as pa


class Table:
    def __init__(self, elem, attrs, tags, name=None):
        self.elem = elem
        self.attrs = attrs
        self.tags = tags
        self.name = name
        


PARSING_SCHEMAS = {
    # ================== 1 ==================
    'GetCompanyArbitrationSummary': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'ArbitrationSummary': [
            'Total', 'Considered', 'Appealed', 'DecisionsAndRulings', 'Completed'
        ],
        'ArbitrationSummary/Plaintiff': [
            'Total', 'TotalSum', 'Considered', 'ConsideredSum', 'Appealed',
            'AppealedSum', 'DecisionsAndRulings', 'DecisionsAndRulingsSum',
            'Completed', 'CompletedSum'
        ],
        'ArbitrationSummary/Defendant': [
            'Total', 'TotalSum', 'Considered', 'ConsideredSum', 'Appealed',
            'AppealedSum', 'DecisionsAndRulings', 'DecisionsAndRulingsSum',
            'Completed', 'CompletedSum'
        ],
        'ArbitrationSummary/Plaintiff/DecisionsAndRulingsByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Plaintiff', '_DecisionsAndRulingsByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/Plaintiff/CompletedByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Plaintiff', '_CompletedByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/Defendant/DecisionsAndRulingsByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Defendant', '_DecisionsAndRulingsByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/Defendant/CompletedByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Defendant', '_CompletedByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/ArbitrationByType': Table(
            'Type',
            ['_Report_SparkID', 'Id', 'Name'],
            {
                'Plaintiff': ['Total', 'Considered', 'Appealed', 'Completed'],
                'Defendant': ['Total', 'Considered', 'Appealed', 'Completed']
            },
            'ByType'
        ),
        'ArbitrationSummary/ArbitrationByYear': Table(
            'Year',
            ['_Report_SparkID', 'Year'],
            {
                'Plaintiff': ['CasesNumber', 'Sum'],
                'Defendant': ['CasesNumber', 'Sum'],
                'ThirdOrOtherPerson': ['CasesNumber']
            },
            'ByYear'
        )
    },
    'GetEntrepreneurArbitrationSummary': {
        'SparkID': [None],
        'FullName': [None],
        'INN': [None],
        'OGRNIP': [None],
        'OKPO': [None],
        'ArbitrationSummary': [
            'Total', 'Considered', 'Appealed', 'DecisionsAndRulings', 'Completed'
        ],
        'ArbitrationSummary/Plaintiff': [
            'Total', 'TotalSum', 'Considered', 'ConsideredSum', 'Appealed', 'AppealedSum',
            'DecisionsAndRulings', 'DecisionsAndRulingsSum', 'Completed', 'CompletedSum'
        ],
        'ArbitrationSummary/Defendant': [
            'Total', 'TotalSum', 'Considered', 'ConsideredSum', 'Appealed', 'AppealedSum',
            'DecisionsAndRulings', 'DecisionsAndRulingsSum', 'Completed', 'CompletedSum'
        ],
        'ArbitrationSummary/Plaintiff/DecisionsAndRulingsByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Plaintiff', '_DecisionsAndRulingsByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/Plaintiff/CompletedByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Plaintiff', '_CompletedByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/Defendant/DecisionsAndRulingsByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Defendant', '_DecisionsAndRulingsByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/Defendant/CompletedByResult': Table(
            'ResultType',
            [
                '_Report_SparkID', '_Defendant', '_CompletedByResult',
                'Id', 'Name', 'CasesNumber', 'Sum'
            ],
            {},
            'FaceResult'
        ),
        'ArbitrationSummary/ArbitrationByType': Table(
            'Type',
            ['_Report_SparkID', 'Id', 'Name'],
            {
                'Plaintiff': ['Total', 'Considered', 'Appealed', 'Completed'],
                'Defendant': ['Total', 'Considered', 'Appealed', 'Completed']
            },
            'ByType'
        ),
        'ArbitrationSummary/ArbitrationByYear': Table(
            'Year',
            ['_Report_SparkID', 'Year'],
            {
                'Plaintiff': ['CasesNumber', 'Sum'],
                'Defendant': ['CasesNumber', 'Sum'],
                'ThirdOrOtherPerson': ['CasesNumber']
            },
            'ByYear'
        )
    },
    'GetCompanyLeasings': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'LeasingsParticipants': Table(
            'Participant',
            ['_Report_SparkID', 'Id', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'BirthDate': [None],
                'Status': ['Code', 'Date', 'IsActing', 'Text']
            },
            'Participants'
        ),
        'Leasings': Table(
            'Leasing',
            [
                '_Report_SparkID', 'Id', 'IsActing', 'IsSublease', 'ContractNumber',
                'ContractDate', 'StartDate', 'EndDate'
            ],
            {
                'StopReason': [None, 'Date'],
                'Lessors/ParticipantId': [None],
                'Lessees/ParticipantId': [None],
                'LeasedProperty': ['ItemsNumber'],
                'LeasedProperty/PropertyType': [None, 'Code']
            }
        )
    },
    'GetEntrepreneurLeasings': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRNIP': [None],
        'OKPO': [None],
        'LeasingsParticipants': Table(
            'Participant',
            ['_Report_SparkID', 'Id', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'BirthDate': [None],
                'Status': ['Code', 'Date', 'IsActing', 'Text']
            }, 'Participants'
        ),
        'Leasings': Table(
            'Leasing',
            [
                '_Report_SparkID', 'Id', 'IsActing', 'IsSublease', 'ContractNumber',
                'ContractDate', 'StartDate', 'EndDate'
            ],
            {
                'StopReason': [None, 'Date'],
                'Lessors/ParticipantId': [None],
                'Lessees/ParticipantId': [None],
                'LeasedProperty': ['ItemsNumber'],
                'LeasedProperty/PropertyType': [None, 'Code']
            }
        )
    },
    'GetLeasingReport': {
        'Leasing': (
            [
                'Id', 'IsActing', 'IsSublease', 'ContractNumber',
                'ContractDate', 'StartDate', 'EndDate'
            ],
            Table(
                'Lessors/Participant',
                ['_Leasing@Id', '_Lessors', 'Type'],
                {
                    'Name': [None],
                    'SparkID': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'BirthDate': [None],
                    'Status': ['IsActing', 'Code', 'Text', 'Date']
                },
                'Report'
            ),
            Table(
                'Lessees/Participant',
                ['_Leasing@Id', '_Lessees', 'Type'],
                {
                    'Name': [None],
                    'SparkID': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'BirthDate': [None],
                    'Status': ['IsActing', 'Code', 'Text', 'Date']
                },
                'Report'
            )
        ),
        'Leasing/StopReason': [None, 'Date'],
        'Leasing/MainContract': ['Number', 'Date'],
        'Leasing/LeasedProperty': Table(
            'Item',
            ['_Leasing@Id', 'Id', 'TypeCode', 'Type', None],
            {},
            'Items'
        )
    },
    'GetCompanySparkRisksReportXML': {
        'SparkID': [None],
        'ShortName': [None],
        'FullName': [None],
        'INN': [None],
        'KPP': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKFS': ['Code', 'Name'],
        'OKVED': ['Code', 'Name', 'IsMain'],
        'Status': ['IsActing', 'Code', 'Text', 'GroupId', 'GroupName', 'Date'],
        'DateFirstReg': [None],
        'CharterCapital': [None, 'ActualDate'],
        'Leader': [
            'ActualDate', 'FIO', 'Position', 'INN', 'LegalCapacityEndDate',
            'ManagementCompany', 'ManagementCompanyINN'
        ],
        'LegalAddress': [
            'PostCode', 'Address', 'Region', 'Rayon', 'City', 'StreetName',
            'BuildingType', 'BuildingNumber', 'HousingType', 'Housing',
            'BlockType', 'Block', 'RoomType', 'Room', 'Longitude', 'Latitude',
            'BusinnesCenterName', 'FiasGUID', 'IsHouseFiasGUID', 'FiasCode',
            'FiasRegion', 'FiasArea', 'FiasCity', 'FiasPlace', 'FiasPlan',
            'FiasStreet', 'ActualDate'
        ],
        'Sites': 'Www',
        'Emails': 'Email',
        'WorkersRange': [None],
        'VacanciesNumber': [None],
        'ConsolidatedIndicator': ['Value', 'Description'],
        'ConsolidatedIndicator/AddInfo': Table(
            'AddField',
            ['_Report_SparkID', 'Id', '_1', None, 'Name'],
            {},
            'AddInfo'
        ),
        'IndexOfDueDiligence': ['Index', 'IndexDesc'],
        'FailureScore': ['FailureScoreValue', 'FailureScoreDesc'],
        'PaymentIndex': ['PaymentIndexValue', 'PaymentIndexDesc'],
        'Registrar/SparkID': [None],
        'Registrar/Name': [None],
        'Registrar/INN': [None],
        'Registrar/OGRN': [None],
        'Registrar/ContractEndDate': [None],
        'HeadOfCompany/SparkID': [None],
        'HeadOfCompany/Name': [None],
        'HeadOfCompany/INN': [None],
        'HeadOfCompany/OGRN': [None],
        'HeadOfCompany/Country/Code': [None],
        'HeadOfCompany/Country/Name': [None],
        'Beneficiary/FIO': [None],
        'Beneficiary/INN': [None],
        'Reorganization/Successor/SparkID': [None],
        'Reorganization/Successor/Name': [None],
        'Reorganization/Successor/Address': [None],
        'Reorganization/Successor/INN': [None],
        'Reorganization/Successor/ORGN': [None],
        'Reorganization/Successor/FullName': [None],
        'Reorganization/Successor/Status': ['IsActing', 'Text', 'Code', 'Date'],
        'ArbitrationCases': [
            'Total', 'Considered', 'Appealed', 'DecisionsAndRulings', 'Completed', 'WonNumber'
        ],
        'ExecutionProceedings': [
            'Active', 'ActiveSum', 'Executed', 'ExecutedSum', 'CompletedNoLocation',
            'CompletedNoProperty', 'CompletedOther', 'TrafficFines'
        ],
        'StructureInfo/ActiveBranchesRosstatNumber': [None],
        'StructureInfo/ActiveAffiliatedCompaniesNumber': ['Source', None],
        'Finance': Table(
            'FinPeriod',
            ['_Report_SparkID','_Finance@BalanceType', 'PeriodName', 'DateBegin', 'DateEnd'],
            {
                'Indicator': ['Name', 'Value', 'IdFinPok']
            }
        ),
        'StateContracts/Tenders': ['AdmittedNumber', 'NotAdmittedNumber', 'WinnerNumber'],
        'StateContracts/Contracts': ['SignedNumber', 'Sum'],
        'Pledger': ['Active', 'Ceased'],
        'Lessee': ['Active', 'Ceased'],
        'MortgagePropertiesNumber': [None],
        'Payments': ['Number', 'PayeesNumber'],
        'RetailTrade': ['CashRegistersNumber', 'SalesPointsNumber'],
        'SubsidiesSum': [None],
        'ActiveLicensesNumber': [None],
        'ActiveTaxiPermitsNumber': [None],
        'ActiveCertificatesNumber': [None],
        'Property': [
            'RealPropertiesNumber', 'RentalPropertiesNumber', 'CustomsWarehousesNumber',
            'DutyFreeShopsNumber'
        ],
        'DomainsNumber': [None],
        'TrademarksNumber': [None],
        'InventionsNumber': [None],
        'IndustrialModelsNumber': [None],
        'ApplicationSoftwareNumber': [None],
        'IntegratedCircuitTopographiesNumber': [None],
        'PatentApplicationNumber': [None],
        'UsingTrademarksNumber': [None],
        'NaturalObjects': ['ForestAreasNumber', 'WaterBodiesNumber', 'WoodDealsNumber'],
        'RegisteredMedia': ['TotalNumber'],
        'Inspections': ['Completed', 'WithViolations', 'Scheduled'],
        'PhoneList': Table(
            'Phone',
            ['_Report_SparkID', 'Code', 'Number', 'Status', 'VerificationDate'],
            {},
            'Phones'
        ),
        'IncludeInList': Table(
            'ListName',
            ['_Report_SparkID', 'Id', None, 'IsNegative'],
            {
                'AddInfo': Table(
                    'AddField',
                    ['_Report_SparkID', '_ListName@Id', '_0', None, 'Name'],
                    {}
                )
            },
            'ListName'
        ),
        'RiskFactors': Table(
            'Factor',
            ['_Report_SparkID', 'Id', 'Name'],
            {
                'AddInfo': Table(
                    'AddField',
                    ['_Report_SparkID', '_Factor@Id', '_2', None, 'Name'],
                    {}
                )
            },
            'Factor'
        ),
        'Auditors': Table(
            'Auditor',
            ['_Report_SparkID'],
            {
                'SparkID': [None],
                'Name': [None],
                'INN': [None],
                'ORGN': [None],
                'ContractYears': 'Year'
            }
        ),
        'FrozenAccounts': Table(
            'Decision',
            ['_Report_SparkID', 'Number', 'Date'],
            {
                'TaxAuthority/Code': [None],
                'TaxAuthority/Name': [None],
                'Bank/BIK': [None],
                'Bank/SparkID': [None],
                'Bank/Name': [None]
            }
        ),
        'MainCoowners': Table(
            'Coowner',
            ['_Report_SparkID'],
            {
                'SparkId': [None],
                'Name': [None],
                'Address': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'FullName': [None],
                'OKATO': [None],
                'SharePart': [None]
            }
        ),
        'FinanceAndTaxesFTS/Period/Taxes': Table(
            'Tax',
            ['_Report_SparkID','_Period@EndDate','Id','Name', 'Sum'],
            {},
            'TaxesFTSDetail'
        ),
        'FinanceAndTaxesFTS': Table(
            'Period',
            ['_Report_SparkID','EndDate'],
            {
                'Income':[None],
                'Expenses':[None],
                'Taxes': ['Sum']
            },
            'TaxesFTS'
        ),
        'SROs': Table(
            'SRO',
            ['_Report_SparkID'],
            {
                'SparkID': [None],
                'Name': [None],
                'INN': [None],
                'OGRN': [None]
            }
        )
    },

    # ================== 2 ==================
    'GetCompanyPledges': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'PledgesParticipants': Table(
            'Participant',
            ['_Report_SparkID', 'Id', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'BitrthDate': [None],
                'Status': ['IsActing', 'Code', 'Text', 'Date']
            }
        ),
        'Pledges': Table(
            'Pledge',
            [
                '_Report_SparkID', 'Id', 'IsActing', 'NotificationNumber',
                'NotificationDate', 'ContractNumber', 'ContractDate', 'PerfomanceDate'
            ],
            {
                'StopReason': ['Date', None],
                'Pledgers': 'ParticipantId',
                'Pledgees': 'ParticipantId',
                'PledgedProperty/PropertyType': ['Code', None]
            }
        )
    },
    'GetEntrepreneurPledges': {
        'SparkID': [None],
        'FullName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'PledgesParticipants': Table(
            'Participant',
            ['_Report_SparkID', 'Id', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'BitrthDate': [None],
                'Status': ['IsActing', 'Code', 'Text', 'Date']
            }
        ),
        'Pledges': Table(
            'Pledge',
            [
                '_Report_SparkID', 'Id', 'IsActing', 'NotificationNumber',
                'NotificationDate', 'ContractNumber', 'ContractDate', 'PerfomanceDate'
            ],
            {
                'StopReason': ['Date', None],
                'Pledgers': 'ParticipantId',
                'Pledgees': 'ParticipantId',
                'PledgedProperty/PropertyType': ['Code', None]
            }
        )
    },
    'GetPledgeReport': {
        'Pledge': [
            'Id', 'IsActing', 'NotificationNumber', 'NotificationDate',
            'ContractNumber', 'ContractDate', 'PerformanceDate'
        ],
        'Pledge/StopReason': ['Date', None],
        'Pledge/Pledgers': Table(
            'Participant',
            ['_0', '_Pledge@Id', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'BirthDate': [None],
                'Status': ['IsActing', 'Code', 'Text', 'Date']
            },
            'Pledges'
        ),
        'Pledge/Pledgees': Table(
            'Participant',
            ['_1', '_Pledge@Id', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'BirthDate': [None],
                'Status': ['IsActing', 'Code', 'Text', 'Date']
            },
            'Pledges'
        ),
        'Pledge/PledgedProperty': Table(
            'Item',
            ['_Pledge@Id', 'TypeCode', 'Type', None],
            {},
            'Items'
        )
    },
    'GetCompanyExecutionProceedings': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'ExecutionProceedings': Table(
            'ExecutionProceeding',
            ['_Report_SparkID', 'IsExecuted'],
            {
                'Number': [None],
                'Date': [None],
                'PayoutAmount': [None],
                'Department': [None],
                'Document': [None],
                'Type': ['GroupId', 'GroupName', 'Id', None],
                'TerminationReason': ['Id', 'Name', 'Date']
            }
        )
    },
    'GetEntrepreneurExecutionProceedings' : {
        'SparkID': [None],
        'FullName': [None],
        'INN': [None],
        'OGRNIP': [None],
        'OKPO': [None],
        'ExecutionProceedings': Table(
            'ExecutionProceeding',
            ['_Report_SparkID', 'IsExecuted'],
            {
                'Number': [None],
                'Date': [None],
                'PayoutAmount': [None],
                'Department': [None],
                'Document': [None],
                'Type': ['GroupId', 'GroupName', 'Id', None],
                'TerminationReason': ['Id', 'Name', 'Date']
            }
        )
    },
    'GetCompanyCounterparties': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'Counterparties': Table(
            'Counterparty',
            ['_Report_SparkID', 'Type'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKATO': ['Code', 'RegionName', 'RegionCode'],
                'Address': [None],
                'Status': ['IsActing', 'Code', 'Text', 'Date'],
                'Sources': Table(
                    'Source',
                    ['_Report_SparkID', '_Counterparty_SparkID', 'Id', 'Name'],
                    {}
                )
            }
        )
    },

    # ================== 3 ==================
    'GetCompanyLicenses': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'EGRPOIncluded': [None],
        'EGRULLikvidation': [None],
        'Licenses': Table(
            'License',
            ['_Company_SparkID'],
            {
                'Number': [None],
                'IssueDate': [None],
                'EndDate': [None],
                'ActivityKind': [None],
                'IssuingAuthority': [None],
                'CurrentStatus': [None],
                'StatusChangeLastDate': [None]
            }
        )
    },
    'GetCompanyFinancialAnalysis': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'GroupId', 'GroupName', 'Date'],
        'FinancialAnalysis': Table(
            'FinPeriod',
            ['_Report_SparkID', 'PeriodName', 'DateBegin', 'DateEnd'],
            {
                'OKVED': ['Code', 'Name']
            }
        ),
        'FinancialAnalysis/FinPeriod': Table(
            'FinIndicators',
            ['_Report_SparkID', '_FinPeriod@PeriodName'],
            {
                'Indicator': [
                    'IdFinPok', 'Name', 'Value', 'MedianValueByIndustry',
                    'AbsoluteDeviation', 'RelativeDeviation'
                ]
            },
            'FinIndicators'
        )
    },
    'GetCompanyRiskFactors': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'GroupId', 'GroupName', 'Date'],
        'ConsolidatedIndicator': Table(
            'AddInfo/AddField',
            [
                '_Report_SparkID', '_ConsolidatedIndicator@Value',
                '_ConsolidatedIndicator@Description', 'Name', None
            ],
            {},
            'ConsolidatedIndicator'
        ),
        'IndexOfDueDiligence': ['Index', 'IndexDesc'],
        'FailureScore': ['FailureScoreValue', 'FailureScoreDesc'],
        'PaymentIndex': ['PaymentIndexValue', 'PaymentIndexDesc'],
        'RiskFactors': Table(
            'Factor/AddInfo/AddField',
            ['_Report_SparkID', '_Factor@Id', '_Factor@Name', 'Name', None],
            {},
            'RiskFactors'
        )
    },
    'GetBankAccountingReport101102_101': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'EGRPOIncluded': [None],
        'Period/Form101': Table(
            'Row',
            ['_Report_SparkID', '_Period@DateEnd', '_Form101@Power'],
            {
                'ORDER': [None],
                'INPARTRUB': [None],
                'INPARTVAL': [None],
                'INPARTTOTAL': [None],
                'OBOROTACTIVRUB': [None],
                'OBOROTAKTIVVAL': [None],
                'OBOROTAKTIVTOTAL': [None],
                'OBOROTPASSIVRUB': [None],
                'OBOROTPASSIVVAL': [None],
                'OBOROTPASSIVTOTAL': [None],
                'OUTPARTRUB': [None],
                'OUTPARTVAL': [None],
                'OUTPARTTOTAL': [None]
            }
        )
    },
    'GetBankAccountingReport101102_102': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'EGRPOIncluded': [None],
        'Period/Form102': Table(
            'Row',
            ['_Report_SparkID', '_Period@DateEnd', '_Form102@Power'],
            {
                'CLAUSENAME': [None],
                'NUMBEROFCLAUSE': [None],
                'VALUETOTAL': [None]
            }
        )
    },
    'GetCompanyPaymentDiscipline': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'PaymentDiscipline/PaymentIndexValues': Table(
            'Period',
            ['_Report_SparkID', 'Name'],
            {
                'PaymentIndex': ['Value', 'Description'],
                'AverageOverdue': [None]
            }
        ),
        'PaymentDiscipline/PaymentIndexDynamics': Table(
            'Period',
            ['_Report_SparkID', 'StartDate', 'EndDate'],
            {
                'PaymentIndex': ['Value', 'Description'],
                'CounterpartiesNumber': [None],
                'InvoicesNumber': [None],
                'Sum': [None]
            }
        ),
        'PaymentDiscipline/InvoicesAnalysis/AnalysisByAmount': Table(
            'AmountRange',
            [
                '_Report_SparkID', '_InvoicesAnalysis@StartDate', '_InvoicesAnalysis@EndDate',
                '_InvoicesAnalysis@InvoicesNumber', '_InvoicesAnalysis@PaidSum',
                '_InvoicesAnalysis@DebtSum', 'MinValue', 'MaxValue'
            ],
            {
                'InvoicesNumber': [None],
                'PaidSum': [None],
                'DebtSum': [None],
                'PaidOnTime': [None],
                'Overdue': Table(
                    'DaysRange',
                    [
                        '_Report_SparkID', '_AnalysisByAmount', '_AmountRange@MinValue',
                        '_AmountRange@MaxValue', '_Industry@Id', '_AmountRange_InvoicesNumber',
                        'MinValue', 'MaxValue'
                    ],
                    {
                        'InvoicesPercent': [None]
                    },
                    'Overdue'
                )
            },
            'AnalysisByAmount'
        ),
        'PaymentDiscipline/InvoicesAnalysis/AnalysisByIndustry': Table(
            'Industry',
            [
                '_Report_SparkID', '_InvoicesAnalysis@StartDate', '_InvoicesAnalysis@EndDate',
                '_InvoicesAnalysis@InvoicesNumber', '_InvoicesAnalysis@PaidSum',
                '_InvoicesAnalysis@DebtSum', 'Id', 'Name'
            ],
            {
                'InvoicesNumber': [None],
                'PaidSum': [None],
                'DebtSum': [None],
                'PaidOnTime': [None],
                'Overdue': Table(
                    'DaysRange',
                    [
                        '_Report_SparkID', '_AnalysisByIndustry', '_AmountRange@MinValue',
                        '_AmountRange@MaxValue', '_Industry@Id', '_Industry_InvoicesNumber',
                        'MinValue', 'MaxValue'
                    ],
                    {
                        'InvoicesPercent': [None]
                    },
                    'Overdue'
                )
            },
            'AnalysisByIndustry'
        )
    },
    'GetCompanyAccountingReport': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'EGRPOIncluded': [None],
        'EGRULLikvidation': [None],
        'Period': (
            ['PeriodName', 'DateBegin', 'DateEnd', 'OKVEDCode', 'ReportType'],
            Table(
                'Form/Value',
                [
                    '_Report_SparkID', '_Period@PeriodName', '_Form@ID',
                    '_Form@Power', 'Code', 'Name', 'Column', None
                ],
                {},
                'Period'
            )
        )
    },
    'GetEntrepreneurShortReport': {
        'SparkID': [None],
        'Status': ['IsActing', 'Code', 'Text', 'GroupId', 'GroupName', 'Date'],
        'DateFirstReg': [None],
        'DateReg': [None],
        'FullNameRus': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': ['Code', 'RegionName', 'RegionCode'],
        'OKTMO': ['Code'],
        'OKOPF': ['Code', 'Name'],
        'OKVED2List': Table(
            'OKVED',
            ['_Report_SparkID', 'Code', 'Name', 'IsMain'],
            {}
        ),
        'PhoneList': Table(
            'Phone',
            ['_Report_SparkID', 'Code', 'Number', 'Status', 'IsOpenData'],
            {}
        ),
        'PaymentIndex': ['PaymentIndexValue', 'PaymentIndexDesc'],
        'FederalTaxRegistration/RegDate': [None],
        'FederalTaxRegistration/RegAuthority': [None],
        'FederalTaxRegistration/RegAuthorityAddress': [None],
        'FederalTaxRegistration/RegAuthorityCode': [None],
        'FederalTaxRegistrationCurrent/RegDate': [None],
        'FederalTaxRegistrationCurrent/RegAuthority': [None],
        'FederalTaxRegistrationCurrent/RegAuthorityAddress': [None],
        'FederalTaxRegistrationCurrent/RegAuthorityCode': [None],
        'FederalTaxRegistrationPayment/RegDate': [None],
        'FederalTaxRegistrationPayment/RegAuthority': [None],
        'FederalTaxRegistrationPayment/RegAuthorityAddress': [None],
        'FederalTaxRegistrationPayment/RegAuthorityCode': [None],
        'RegistrationInFunds/PensionFund/RegistrationDate': [None],
        'RegistrationInFunds/PensionFund/DeregistrationDate': [None],
        'RegistrationInFunds/PensionFund/RegisterNumber': [None],
        'RegistrationInFunds/PensionFund/RegAuthority': [None],
        'RegistrationInFunds/SocialInsuranceFund/RegistrationDate': [None],
        'RegistrationInFunds/SocialInsuranceFund/DeregistrationDate': [None],
        'RegistrationInFunds/SocialInsuranceFund/RegisterNumber': [None],
        'RegistrationInFunds/SocialInsuranceFund/RegAuthority': [None],
        'SubmittedStatements': Table(
            'Statement',
            [
                '_Report_SparkID', 'Form', 'ReferenceNumber', 'SubmissionDate',
                'AvailabilityDate', 'GRN', 'DecisionType'
            ],
            {}
        ),
        'RegistrationCertificates': Table(
            'RegistrationCertificate',
            ['_Report_SparkID', 'Series', 'Number', 'IssueDate', 'GRN'],
            {}
        ),
        'BirthDate': [None],
        'BirthPlace': [None],
        'Sex': ['Code', 'Name'],
        'Citizenship': ['Code', 'Code'],
        'LinkedOGRNIP': Table(
            'OGRNIP',
            ['_Report_SparkID', None, 'IsActing'],
            {}
        ),
        'IncludeInList': (
            Table(
                'ListName',
                ['_Report_SparkID', 'Id', 'IsNegative', None],
                {}
            ),
            Table(
                'ListName/AddInfo/AddField',
                ['_Report_SparkID', '_ListName@Id', 'Name', None],
                {},
                'IncludeInList_AddInfo'
            )
        ),
        'FrozenAccounts': Table(
            'Decision',
            ['_Report_SparkID', 'Number', 'Date'],
            {
                'Reason': ['Id', 'Name'],
                'TaxAuthority/Code': [None],
                'TaxAuthority/Name': [None],
                'Bank/BIK': [None],
                'Bank/SparkID': [None],
                'Bank/Name': [None]
            }
        ),
        'StateContracts/FederalLaw94': Table(
            'Year',
            ['_Report_SparkID', '_94', 'Year'],
            {
                'Tenders': ['AdmittedNumber', 'NotAdmittedNumber', 'WinnerNumber'],
                'Contracts': ['SignedNumber', 'Sum']
            },
            'StateContracts'
        ),
        'StateContracts/FederalLaw223': Table(
            'Year',
            ['_Report_SparkID', '_223', 'Year'],
            {
                'Tenders': ['AdmittedNumber', 'NotAdmittedNumber', 'WinnerNumber'],
                'Contracts': ['SignedNumber', 'Sum']
            },
            'StateContracts'
        ),
        'ArbitrationCases': Table(
            'Year',
            [
                '_Report_SparkID', '_ArbitrationCases@Total', '_ArbitrationCases@Considered',
                '_ArbitrationCases@Appealed', '_ArbitrationCases@DecisionsAndRulings',
                '_ArbitrationCases@Completed', 'Year'
            ],
            {
                'Plaintiff': ['CasesNumber', 'Sum'],
                'Defendant': ['CasesNumber', 'Sum'],
                'ThirdOrOtherPerson': ['CasesNumber']
            }
        ),
        'BankruptcyMessage': Table(
            'Message',
            [
                '_Report_SparkID', 'Id', 'Date', 'DecisionDate', 'IdType', 'Type',
                'CanceledMessageId', 'IsCanceled', 'CaseId', 'CaseNumber'
            ],
            {}
        ),
        'BankruptcyArbitrationCases': Table(
            'ArbitrationCase',
            [
                '_Report_SparkID', 'Id', 'Number', 'StatusId', 'StatusName', 'RegistrationDate',
                'AcceptanceDate', 'SupervisionDate', 'FinancialRecoveryDate',
                'ExternalManagementDate', 'BankruptcyProceedingsDate', 'CompleteDate'
            ],
            {}
        ),
        'ExecutionProceedings': ['Active', 'Executed'],
        'Pledges/Pledger': ['Active', 'Ceased'],
        'Pledges/Pledgee': ['Active', 'Ceased'],
        'Disqualifications': Table(
            'Disqualification',
            [
                '_Report_SparkID', 'RegisterNumber', 'Article', 'StartDate', 'EndDate', 'Period',
                'DisqualifedInCompany'
            ],
            {}
        )
    },
    'GetCompanyExtendedReport': {
        'SparkID': [None],
        'CompanyType': [None],
        'Status': ['IsActing', 'Code', 'Type', 'GroupId', 'GroupName', 'Date'],
        'EGRPOIncluded': [None],
        'EGRULLikvidation': [None],
        'IsActing': [None],
        'DateFirstReg': [None],
        'ShortName': [None],
        'ShortNameRus': [None],
        'ShortNameEn': [None],
        'FullNameRus': [None],
        'NormName': [None],
        'GUID': [None],
        'INN': [None],
        'KPP': [None],
        'OGRN': [None],
        'OKPO': [None],
        'BIK': [None],
        'FCSMCode': [None],
        'RTS': [None],
        'OKATO': ['Code', 'RegionName', 'RegionCode'],
        'OKTMO': ['Code'],
        'OKOGU': ['Code'],
        'OKOGU': ['Code', 'Name'],
        'OKFS': ['Code', 'Name'],
        'OKOPF': ['Code', 'CodeNew', 'Name'],
        'OKVED2List': Table(
            'OKVED',
            ['_Report_SparkID', 'Code', 'Name', 'IsMain', 'IsMainEGRUL', 'IsMainRosstat'],
            {}
        ),
        'ChangesInNameAndLegalForm': Table(
            'Change',
            ['_Report_SparkID'],
            {
                'Name': [None],
                'OGRN': [None],
                'INN': [None],
                'OKOPF': ['Code', 'CodeNew', 'Name'],
                'ChangeDate': [None]
            }
        ),
        'CharterCapital': [None],
        'CharterCapitalHistory': Table(
            'CharterCapital',
            ['_Report_SparkID', 'ActualDate', None],
            {}
        ),
        'LeaderList': Table(
            'Leader',
            [
                '_Report_SparkID', 'ActualDate', 'FIO',
                'Position', 'INN', 'LegalCapacityEndDate',
                'ManagementCompany', 'ManagementCompanyINN'
            ],
            {
                'Disqualification': [
                    'RegisterNumber', 'Article', 'StartDate', 'EndDate',
                    'Period', 'DisqualifiedInCompany'
                ]
            }
        ),
        'LegalAddresses': Table(
            'Address',
            [
                '_Report_SparkID', '_LegalAddresses', 'PostCode', 'Address', 'Region', 'Rayon',
                'City', 'StreetName', 'BuildingType', 'BuildingNumber', 'HousingType', 'Housing',
                'RoomType', 'Room', 'Longitude', 'Latitude', 'FiasGUID', 'IsHouseFiasGUID',
                'FiasCode', 'FiasRegion', 'FiasArea', 'FiasCity', 'FiasPlace', 'FiasPlan',
                'FiasStreet', 'ActualDate', 'BlockType', 'Block', 'BusinessCenterName'
            ],
            {},
            'Addresses'
        ),
        'AdjustAddresses': Table(
            'Address',
            [
                '_Report_SparkID', '_AdjustAddresses', 'PostCode', 'Address', 'Region', 'Rayon',
                'City', 'StreetName', 'BuildingType', 'BuildingNumber', 'HousingType', 'Housing',
                'RoomType', 'Room', 'Longitude', 'Latitude', 'FiasGUID', 'IsHouseFiasGUID',
                'FiasCode', 'FiasRegion', 'FiasArea', 'FiasCity', 'FiasPlace', 'FiasPlan',
                'FiasStreet', 'ActualDate', 'BlockType', 'Block', 'BusinessCenterName'
            ],
            {},
            'Addresses'
        ),
        'PreviousAddress': Table(
            'Address',
            [
                '_Report_SparkID', '_PreviousAddress', 'PostCode', 'Address', 'Region', 'Rayon',
                'City', 'StreetName', 'BuildingType', 'BuildingNumber', 'HousingType', 'Housing',
                'RoomType', 'Room', 'Longitude', 'Latitude', 'FiasGUID', 'IsHouseFiasGUID',
                'FiasCode', 'FiasRegion', 'FiasArea', 'FiasCity', 'FiasPlace', 'FiasPlan',
                'FiasStreet', 'ActualDate', 'BlockType', 'Block', 'BusinessCenterName'
            ],
            {},
            'Addresses'
        ),
        'PhoneList': Table(
            'Phone',
            [
                '_Report_SparkID', '_Номера компании', 'Code', 'Number', 'Status',
                'VerificationDate', 'IsOpenData', 'Value'
            ],
            {}
        ),
        'Email': [None],
        'Www': [None],
        'WorkersRange': [None],
        'StaffNumberFTS': Table(
            'Number',
            ['_Report_SparkID', 'ActualDate', None],
            {}
        ),
        'IncludeInList': (
            Table(
                'ListName',
                ['_Report_SparkID', 'Id', 'IsNegative', None],
                {}
            ),
            Table(
                'ListName/AddInfo/AddField',
                ['_Report_SparkID', '_ListName@Id', 'Name', None],
                {},
                'IncludeInList_AddInfo'
            )
        ),
        'ConsolidatedIndicator': Table(
            'AddInfo/AddField',
            [
                '_Report_SparkID', '_ConsolidatedIndicator@Value',
                '_ConsolidatedIndicator@Description', 'Name', None
            ],
            {}
        ),
        'IndexOfDueDiligence': ['Index', 'IndexDesc'],
        'FailureScore': ['FailureScoreValue', 'FailureScoreDesc'],
        'PaymentIndex': ['PaymentIndexValue', 'PaymentIndexDesc'],
        'CreditLimit': ['Value', 'Description'],
        'CompanySize': ['Revenue', 'Description', 'ActualDate'],
        'FederalTaxRegistration/RegDate': [None],
        'FederalTaxRegistration/RegAuthority': [None],
        'FederalTaxRegistration/RegAuthorityAddress': [None],
        'FederalTaxRegistration/RegAuthorityCode': [None],
        'FederalTaxRegistrationCurrent/RegDate': [None],
        'FederalTaxRegistrationCurrent/RegAuthority': [None],
        'FederalTaxRegistrationCurrent/RegAuthorityAddress': [None],
        'FederalTaxRegistrationCurrent/RegAuthorityCode': [None],
        'FederalTaxRegistrationPayment/RegDate': [None],
        'FederalTaxRegistrationPayment/RegAuthority': [None],
        'FederalTaxRegistrationPayment/RegAuthorityAddress': [None],
        'FederalTaxRegistrationPayment/RegAuthorityCode': [None],
        'RegisterNumber': [None],
        'SpecialTaxRegimes': Table(
            'Regime',
            ['_Report_SparkID', '_SpecialTaxRegimes@ActualDate', 'Code', 'Name'],
            {}
        ),
        'RegistrationInFunds/PensionFund/RegistrationDate': [None],
        'RegistrationInFunds/PensionFund/DeregistrationDate': [None],
        'RegistrationInFunds/PensionFund/RegisterNumber': [None],
        'RegistrationInFunds/PensionFund/RegAuthority': [None],
        'RegistrationInFunds/SocialInsuranceFund/RegistrationDate': [None],
        'RegistrationInFunds/SocialInsuranceFund/DeregistrationDate': [None],
        'RegistrationInFunds/SocialInsuranceFund/RegisterNumber': [None],
        'RegistrationInFunds/SocialInsuranceFund/RegAuthority': [None],
        'RegistrationInFunds/CompulsoryMedicalInsuranceFund/RegistrationDate': [None],
        'RegistrationInFunds/CompulsoryMedicalInsuranceFund/DeregistrationDate': [None],
        'RegistrationInFunds/CompulsoryMedicalInsuranceFund/RegisterNumber': [None],
        'RegistrationInFunds/CompulsoryMedicalInsuranceFund/RegAuthority': [None],
        'SubmittedStatements': Table(
            'Statement',
            [
                '_Report_SparkID', 'Form', 'ReferenceNumber', 'SubmissionDate',
                'AvailabilityDate', 'GRN', 'DecisionType'
            ],
            {}
        ),
        'RegistrationCertificates': Table(
            'RegistrationCertificate',
            ['_Report_SparkID', 'Series', 'Number', 'IssueDate', 'GRN'],
            {}
        ),
        'StructureInfo/CountCoownerFCSM': [None],
        'StructureInfo/CountCoownerRosstat': [None],
        'StructureInfo/CountCoownerEGRUL': [None],
        'StructureInfo/CountBranch': [None],
        'StructureInfo/CountBranchRosstat': [None],
        'StructureInfo/CountBranchEGRUL': [None],
        'StructureInfo/CountAffiliatedCompanyFCSM': [None],
        'StructureInfo/CountAffiliatedCompanyRosstat': [None],
        'StructureInfo/CountAffiliatedCompanyEGRUL': [None],
        'StructureInfo/NonprofitOrganizationRosstat': [None],
        'AffiliatedCompaniesRosstat': Table(
            'AffiliatedCompanyRosstat',
            [
                '_Report_SparkID', '_AffiliatedCompaniesRosstat',
                '_AffiliatedCompaniesRosstat@ActualDate'
            ],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'SharePart': [None]
            },
            'AffiliatedCompanies'
        ),
        'AffiliatedCompaniesFCSM': Table(
            'AffiliatedCompanyRosstat',
            [
                '_Report_SparkID', '_AffiliatedCompaniesFCSM',
                '_AffiliatedCompaniesFCSM@ActualDate'
            ],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'SharePart': [None]
            },
            'AffiliatedCompanies'
        ),
        'AffiliatedCompaniesEGRUL': Table(
            'AffiliatedCompanyRosstat',
            [
                '_Report_SparkID', '_AffiliatedCompaniesEGRUL',
                '_AffiliatedCompaniesEGRUL@ActualDate'
            ],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'SharePart': [None]
            },
            'AffiliatedCompanies'
        ),
        'CoownersFCSM': Table(
            'CoownerFCSM',
            [
                '_Report_SparkID', '_CoownersFCSM', '_CoownersFCSM@ShareHolderCount',
                '_CoownersFCSM@ActualDate'
            ],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'Country': ['Code', 'Name'],
                'TypeHolder': [None],
                'IsCompany': [None],
                'SharePart': [None]
            },
            'Coowners'
        ),
        'CoownersRosstat': Table(
            'CoownerRosstat',
            [
                '_Report_SparkID', '_CoownersRosstat', '_CoownersRosstat@ShareHolderCount',
                '_CoownersRosstat@ActualDate'
            ],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'Country': ['Code', 'Name'],
                'TypeHolder': [None],
                'IsCompany': [None],
                'SharePart': [None]
            },
            'Coowners'
        ),
        'CoownersEGRUL': Table(
            'CoownerEGRUL',
            [
                '_Report_SparkID', '_CoownersEGRUL', '_CoownersEGRUL@ShareHolderCount',
                '_CoownersEGRUL@ActualDate'
            ],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'Country': ['Code', 'Name'],
                'TypeHolder': [None],
                'IsCompany': [None],
                'SharePart': [None]
            },
            'Coowners'
        ),
        'Branches': Table(
            'Branch',
            ['_Report_SparkID', '_Branches'],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'OpenDate': [None],
                'TermDate': [None]
            },
            'Branches'
        ),
        'BranchesRosstat': Table(
            'BranchRosstat',
            ['_Report_SparkID', '_BranchesRosstat'],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKATO': [None],
                'OpenDate': [None],
                'TermDate': [None]
            },
            'Branches'
        ),
        'BranchesEgrul': Table(
            'BranchRosstat',
            ['_Report_SparkID'],
            {
                'Address': [None]
            }
        ),
        'NonprofitOrganizationsRosstat': Table(
            'NonprofitOrganizationRosstat',
            ['_Report_SparkID', '_NonprofitOrganizationsRosstat'],
            {
                'Fullname': [None],
                'Name': [None],
                'Address': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OpenDate': [None],
                'TermDate': [None]
            },
            'Branches'
        ),
        'Finance': Table(
            'FinPeriod/StringList/String',
            [
                '_Report_SparkID', '_Finance@BalanceType', '_FinPeriod@PeriodName',
                '_FinPeriod@DateBegin', '_FinPeriod@DateEnd', 'Form', 'Section',
                'Name', 'Code', 'Value', 'IdFinPok'
            ],
            {},
            'Finance'
        ),
        'CompanyWithSameInfo/TelephoneCount': [None, 'PhoneCode', 'PhoneNumber'],
        'CompanyWithSameInfo/AddressCount': [None],
        'CompanyWithSameInfo/AddressWithoutRoomCount': [None],
        'CompanyWithSameInfo/AddressNotAffiliatedCount': [None],
        'CompanyWithSameInfo/AddressFTSCount': [None],
        'CompanyWithSameInfo/ManagerCountInCountry': [None],
        'CompanyWithSameInfo/ManagerCountInRegion': [None],
        'CompanyWithSameInfo/ManagerInnCount': [None],
        'CompanyWithSameInfo/PhoneList': Table(
            'PhoneCount',
            [
                '_Report_SparkID', '_Компании с аналогичными данными', 'Code', 'Number',
                'Status', 'VerificationDate', 'IsOpenData', None
            ],
            {},
            'PhoneList'
        ),
        'CompanyLiquidatedWithSameInfo/AddressCount': [None],
        'CompanyLiquidatedWithSameInfo/AddressWithoutRoomCount': [None],
        'BoardOfDirectors': Table(
            'Member',
            ['_Report_SparkID', '_BoardOfDirectors', '_BoardOfDirectors@ActualDate'],
            {
                'Name': [None],
                'INN': [None],
                'BirthdayYear': [None],
                'Position': ['Code', 'Name'],
                'SharePart': [None]
            },
            'BoardOfDirectors_ExecutiveBody'
        ),
        'ExecutiveBody': Table(
            'Member',
            ['_Report_SparkID', '_ExecutiveBody', '_ExecutiveBody@ActualDate'],
            {
                'Name': [None],
                'INN': [None],
                'BirthdayYear': [None],
                'Position': ['Code', 'Name'],
                'SharePart': [None]
            },
            'BoardOfDirectors_ExecutiveBody'
        ),
        'PersonsWithoutWarrant': Table(
            'Person',
            [
                '_Report_SparkID', '_PersonsWithoutWarrant@ActualDate', 'FIO', 'Position',
                'INN', 'LegalCapacityEndDate'
            ],
            {},
            'PersonsWithoutWarrant'
        ),
        'StateContracts/FederalLaw94': Table(
            'Year',
            ['_Report_SparkID', '_94', 'Year'],
            {
                'Tenders': ['AdmittedNumber', 'NotAdmittedNumber', 'WinnerNumber'],
                'Contracts': ['SignedNumber', 'Sum']
            },
            'StateContracts'
        ),
        'StateContracts/FederalLaw223': Table(
            'Year',
            ['_Report_SparkID', '_223', 'Year'],
            {
                'Tenders': ['AdmittedNumber', 'NotAdmittedNumber', 'WinnerNumber'],
                'Contracts': ['SignedNumber', 'Sum']
            },
            'StateContracts'
        ),
        'ArbitrationCases': Table(
            'Year',
            [
                '_Report_SparkID', '_ArbitrationCases@Total', '_ArbitrationCases@Considered',
                '_ArbitrationCases@Appealed', '_ArbitrationCases@DecisionsAndRulings',
                '_ArbitrationCases@Completed', 'Year'
            ],
            {
                'Plaintiff': ['CasesNumber', 'Sum'],
                'Defendant': ['CasesNumber', 'Sum'],
                'ThirdOrOtherPerson': ['CasesNumber']
            }
        ),
        'BankruptcyMessage': Table(
            'Message',
            [
                '_Report_SparkID', 'Id', 'Date', 'DecisionDate',
                'IdType', 'Type', 'CaseId', 'CaseNumber'
            ],
            {}
        ),
        'BankruptcyArbitrationCases': Table(
            'ArbitrationCase',
            [
                '_Report_SparkID', 'Id', 'Number', 'StatusId', 'StatusName', 'RegistrationDate',
                'AcceptanceDate', 'SupervisionDate', 'ExternalManagementDate',
                'BankruptcyProceedingsDate', 'CompleteDate'
            ],
            {}
        ),
        'FinanceAndTaxesFTS': Table(
            'Period',
            [],
            {
                'Taxes': Table(
                    'Tax',
                    [
                        '_Report_SparkID', '_Taxes','_Period_Income','_Period_Expenses',
                        '_Period@EndDate', '_Taxes@Sum', 'Id', 'Name', 'Sum','DebtSum',
                        'FinesSum', 'PenaltiesSum' 
                    ],
                    {},
                    'FinanceAndTaxesFTS'
                ),
                'TaxArrears': Table(
                    'Tax',
                    [
                        '_Report_SparkID', '_TaxArrears','_Period_Income','_Period_Expenses',
                        '_Period@EndDate', '_TaxArrears@Sum', 'Id', 'Name', 'Sum', 'DebtSum',
                        'FinesSum', 'PenaltiesSum' 
                    ],
                    {},
                    'FinanceAndTaxesFTS'
                ),
                'TaxPenalties':
                    [
                        '_Report_SparkID', '_TaxPenalties','_Period_Income','_Period_Expenses',
                        '_Period@EndDate', 'Sum', 'Id', 'Name', 'Summ', 'DebtSum',
                        'FinesSum', 'PenaltiesSum' 
                    ],
                
            }
        ),
        'AccessibleFinData': Table(
            'Period',
            ['_Report_SparkID', 'IDPeriod', 'Name', 'EndDate'],
            {}
        ),
        'FrozenAccounts': Table(
            'Decision',
            ['_Report_SparkID', 'Number', 'Date'],
            {
                'Reason': ['Id', 'Name'],
                'TaxAuthority/Code': [None],
                'TaxAuthority/Name': [None],
                'Bank/BIK': [None],
                'Bank/SparkID': [None],
                'Bank/Name': [None]
            }
        ),
        'CompanyLiquidatedWithSameInfo/AddressCount': [None],
        'CompanyLiquidatedWithSameInfo/AddressWithoutRoomCount': [None],
        'ExecutionProceedings': ['Active', 'Executed'],
        'Pledges/Pledger': ['Active', 'Ceased'],
        'Pledges/Pledgee': ['Active', 'Ceased']
    },

    # ================== 4 ==================
    'GetCompanyBeneficiariesAndAffiliates': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'Beneficiaries': Table(
            'Beneficiary',
            ['_Report_SparkID', '_Beneficiaries', 'Type', 'IsFinal'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'Country': ['Code', 'Name'],
                'NotFinalReason': ['Id', 'Name']
            },
            'BeneficiariesAndAffiliates'
        ),
        'Affiliates': Table(
            'Affiliate',
            ['_Report_SparkID', '_Affiliates', 'Type', 'IsFinal'],
            {
                'Name': [None],
                'SparkID': [None],
                'INN': [None],
                'OGRN': [None],
                'Country': ['Code', 'Name'],
                'NotFinalReason': ['Id', 'Name']
            },
            'BeneficiariesAndAffiliates'
        )
    },
    'GetOwnershipHierarchy': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'EDRPU': [None],
        'RNN': [None],
        'BIN': [None],
        'OKATO': [None],
        'EGRPOIncluded': [None],
        'EGRULLikvidation': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'Coowners': Table(
            'Coowner',
            ['_Report_SparkID'],
            {
                'Id': [None],
                'ParentId': [None],
                'Level': [None],
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'Country': ['Code', 'Name'],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPF':['Code','Name','CodeNew'],
                'OKATO': [None],
                'EDRPU': [None],
                'RNN': [None],
                'Manager': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'IndirectSharePart': [None],
                'CoownerType': [None],
                'ActualDate': [None]
            }
        )
    },
    'GetCompanyStructure': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'EGRPOIncluded': [None],
        'EGRULLikvidation': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'CoownersRosstat': Table(
            'CoownerRosstat',
            [
                '_Report_SparkID', '_CoownerRosstat', '_CoownersRosstat@ActualDate',
                '_CoownersRosstat@ShareHoldersCount'
            ],
            {
                'Name': [None],
                'SparkID': [None],
                'AddressOrComment': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'FullName': [None],
                'OKATO': [None],
                'Country': ['Code','Name'],
                'TypeHolder': [None],
                'IsCompany': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'LegalCapacityEndDate': [None],
                'InputDate': [None],
                'CoownerType': [None],
            },
            'Coowners'
        ),
        'CoownersEGRUL': Table(
            'CoownerEGRUL',
            [
                '_Report_SparkID', '_CoownerEGRUL', '_CoownersEGRUL@ActualDate',
                '_CoownersEGRUL@ShareHoldersCount'
            ],
            {
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'FullName': [None],
                'OKATO': [None],
                'Country': ['Code','Name'],
                'TypeHolder': [None],
                'IsCompany': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'LegalCapacityEndDate': [None],
                'InputDate': [None],
                'CoownerType': [None],
                'ChargeOfSharePart': Table(
                    'Pledge',
                    [
                        '_Report_SparkID', '_CoownerEGRUL_INN', 'ContractNumber',
                        'ContractDate', 'RegistrationDate', 'GRN'
                    ],
                    {
                        'NotaryFIO': [None],
                        'Term': [None],
                        'Pledgee/Name': [None],
                        'Pledgee/SparkID': [None],
                        'Pledgee/INN': [None],
                        'Pledgee/OGRN': [None]
                    },
                    'CoownerEGRUL_Pledge'
                )
            },
            'Coowners'
        ),
        'CoownersFCSM': Table(
            'CoownerFCSM',
            [
                '_Report_SparkID', '_CoownerFCSM', '_CoownersFCSM@ActualDate',
                '_CoownersFCSM@ShareHoldersCount'
            ],
            {
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'FullName': [None],
                'OKATO': [None],
                'Country': ['Code', 'Name'],
                'TypeHolder': [None],
                'IsCompany': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'LegalCapacityEndDate': [None],
                'InputDate': [None],
                'CoownerType': [None],
            },
            'Coowners'
        ),
        'BranchesRosstat': Table(
            'BranchRosstat',
            ['_Report_SparkID', '_BranchRosstat'],
            {
                'Name': [None],
                'SparkID': [None],
                'AddressOrComment': [None],
                'OpenDate': [None],
                'TermDate': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None],
                'KPP': [None],
                'Address': [None]  
            },
            'Branch'
        ),
        'Branches': Table(
            'Branch',
            ['_Report_SparkID', '_Branch'],
            {
                'Name': [None],
                'SparkID': [None],
                'AddressOrComment': [None],
                'OpenDate': [None],
                'TermDate': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None],
                'KPP': [None],
                'Address': [None]  
            },
            'Branch'
        ),
        'BranchesEGRUL': Table(
            'BranchEGRUL',
            ['_Report_SparkID', '_BranchEGRUL'],
            {
                'Name': [None],
                'SparkID': [None],
                'AddressOrComment': [None],
                'OpenDate': [None],
                'TermDate': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None],
                'KPP': [None],
                'Address': [None]  
            },
            'Branch'
        ),
        'AffiliatedCompaniesFCSM': Table(
            'AffiliatedCompanyFCSM',
            [
                '_Report_SparkID', '_AffiliatedCompanyFCSM',
                '_AffiliatedCompaniesFCSM@ActualDate'
            ],
            {
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None],
                'ActualDate': [None]
            },
            'AffiliatedCompanies'
        ),
        'AffiliatedCompaniesEGRUL': Table(
            'AffiliatedCompanyEGRUL',
            [
                '_Report_SparkID', '_AffiliatedCompanyEGRUL',
                '_AffiliatedCompaniesEGRUL@ActualDate'
            ],
            {
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None],
                'ActualDate': [None]
            },
            'AffiliatedCompanies'
        ),
        'AffiliatedCompaniesRosstat': Table(
            'AffiliatedCompanyRosstat',
            [
                '_Report_SparkID', '_AffiliatedCompanyRosstat',
                '_AffiliatedCompaniesRosstat@ActualDate'
            ],
            {
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'SharePart': [None],
                'SharePartRUR': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None],
                'ActualDate': [None]
            },
            'AffiliatedCompanies'
        ),
        'NonprofitOrganizationsRosstat': Table(
            'NonprofitOrganizationRosstat',
            ['_Report_SparkID'],
            {
                'Name': [None],
                'SparkID': [None],
                'Address': [None],
                'INN': [None],
                'OGRN': [None],
                'OKPO': [None],
                'Manager': [None],
                'ManagerInn': [None],
                'OKOPFName': [None],
                'FullName': [None],
                'OKATO': [None]
            },
            'NonprofitOrganizationsRosstat'
        )
    },
    'GetCompanyPredecessorSuccessor': {
        'SparkID': [None],
        'ShortName': [None],
        'INN': [None],
        'OGRN': [None],
        'OKPO': [None],
        'OKATO': [None],
        'Status': ['IsActing', 'Code', 'Text', 'Date'],
        'Reorganizations': (
            Table(
                'Predecessor',
                ['_Report_SparkID', '_Predecessor', '_0'],
                {
                    'SparkID': [None],
                    'Name': [None],
                    'Address': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'FullName': [None],
                    'Status': ['IsActing', 'Text', 'Code', 'Date']
                },
                'Reorganizations'
            ),
            Table(
                'Successor',
                ['_Report_SparkID', '_Successor', '_0'],
                {
                    'SparkID': [None],
                    'Name': [None],
                    'Address': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'FullName': [None],
                    'Status': ['IsActing', 'Text', 'Code', 'Date']
                },
                'Reorganizations'
            ),
            Table(
                'Participant',
                ['_Report_SparkID', '_Participant', '_0'],
                {
                    'SparkID': [None],
                    'Name': [None],
                    'Address': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'FullName': [None],
                    'Status': ['IsActing', 'Text', 'Code', 'Date']
                },
                'Reorganizations'
            ),
            Table(
                'Current/Predecessor',
                ['_Report_SparkID', '_Predecessor', '_1'],
                {
                    'SparkID': [None],
                    'Name': [None],
                    'Address': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'FullName': [None],
                    'Status': ['IsActing', 'Text', 'Code', 'Date']
                },
                'Reorganizations'
            ),
            Table(
                'Current/Successor',
                ['_Report_SparkID', '_Successor', '_1'],
                {
                    'SparkID': [None],
                    'Name': [None],
                    'Address': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'FullName': [None],
                    'Status': ['IsActing', 'Text', 'Code', 'Date']
                },
                'Reorganizations'
            ),
            Table(
                'Current/Participant',
                ['_Report_SparkID', '_Participant', '_1'],
                {
                    'SparkID': [None],
                    'Name': [None],
                    'Address': [None],
                    'INN': [None],
                    'OGRN': [None],
                    'FullName': [None],
                    'Status': ['IsActing', 'Text', 'Code', 'Date']
                },
                'Reorganizations'
            )
        )
    },
    'OrderCompanyBeneficiariesAndAffiliates': {
        'OrderID': [None]
    }
}


XML_ROOT_ELEMENT = {
    # ================== 1 ==================
    'GetCompanyArbitrationSummary': 'Data/Report',
    'GetEntrepreneurArbitrationSummary': 'Data/Report',
    'GetCompanyLeasings': 'Data/Report',
    'GetEntrepreneurLeasings': 'Data/Report',
    'GetLeasingReport': 'Data',
    'GetCompanySparkRisksReportXML': 'Data/Report',

    # ================== 2 ==================
    'GetCompanyPledges': 'Data/Report',
    'GetEntrepreneurPledges': 'Data/Report',
    'GetPledgeReport': 'Data',
    'GetCompanyExecutionProceedings': 'Data/Report',
    'GetEntrepreneurExecutionProceedings': 'Data/Report',
    'GetCompanyCounterparties': 'Data/Report',
    
    # ================== 3 ==================
    'GetCompanyLicenses': 'Data/Company',
    'GetCompanyFinancialAnalysis': 'Data/Report',
    'GetCompanyRiskFactors': 'Data/Report',
    'GetBankAccountingReport101102_101': 'Data/Report',
    'GetBankAccountingReport101102_102': 'Data/Report',
    'GetCompanyPaymentDiscipline': 'Data/Report',
    'GetCompanyAccountingReport': 'Data/Report',
    'GetEntrepreneurShortReport': 'Data/Report',
    'GetCompanyExtendedReport': 'Data/Report',

    # ================== 4 ======================
    'GetCompanyBeneficiariesAndAffiliates': 'Data/Report',
    'GetOwnershipHierarchy': 'Data/Report',
    'GetCompanyStructure': 'Data/Report',
    'GetCompanyPredecessorSuccessor': 'Data/Report',
    'OrderCompanyBeneficiariesAndAffiliates': 'Data'
}


CALC_PARTITION_SIZE = {
    # ================== 1 ==================
    'GetCompanyArbitrationSummary': 3500,
    'GetEntrepreneurArbitrationSummary': 200000,
    'GetCompanyLeasings': 200000,
    'GetEntrepreneurLeasings': 200000,
    'GetLeasingReport': 200000,
    'GetCompanySparkRisksReportXML': 100000,

    # ================== 2 ==================
    'GetCompanyPledges': 200000,
    'GetEntrepreneurPledges': 200000,
    'GetPledgeReport': 200000,
    'GetCompanyExecutionProceedings': 200000,
    'GetEntrepreneurExecutionProceedings': 200000,
    'GetCompanyCounterparties': 200000,

    # ================== 3 ==================
    'GetCompanyLicenses': 200000,
    'GetCompanyFinancialAnalysis': 200000,
    'GetCompanyRiskFactors': 200000,
    'GetBankAccountingReport101102_101': 200000,
    'GetBankAccountingReport101102_102': 200000,
    'GetCompanyPaymentDiscipline': 200000,
    'GetCompanyAccountingReport': 100000,
    'GetEntrepreneurShortReport': 200000,
    'GetCompanyExtendedReport': 50000,

    # ================== 4 ======================
    'GetCompanyBeneficiariesAndAffiliates': 200000,
    'GetOwnershipHierarchy': 200000,
    'GetCompanyStructure': 200000,
    'GetCompanyPredecessorSuccessor': 200000,
    'OrderCompanyBeneficiariesAndAffiliates': 200000,
    'CheckCompanyStatus': 200000
}


CAST_TYPES_INDEXES = {
    # ================== 1 ==================
    'GetCompanyArbitrationSummary': {
        'Main': {
            'bool': 6,
            'float': [
                16, 18, 20, 22, 24,
                26, 28, 30, 32, 34
            ],
            'int': [
                10, 11, 12, 13, 14,
                15, 17, 19, 21, 23,
                25, 27, 29, 31, 33
            ]
        },
        'FaceResult': {
            'float': 6,
            'int': 5
        },
        'ByType': {
            'int': [3, 4, 5, 6, 7, 8, 9, 10]
        },
        'ByYear': {
            'float': [3, 5],
            'int': [2, 4, 6]
        }
    },
    'GetEntrepreneurArbitrationSummary': {
        'Main': {
            'float': [
                11, 13, 15, 17, 19,
                21, 23, 25, 27, 29
            ],
            'int': [
                5,  6,  7,  8,  9,
                10, 12, 14, 16, 18,
                20, 22, 24, 26, 28
            ]
        },
        'FaceResult': {
            'float': 6,
            'int': 5
        },
        'ByType': {
            'int': [3, 4, 5, 6, 7, 8, 9, 10]
        },
        'ByYear': {
            'float': [3, 5],
            'int': [2, 4, 6]
        }
    },
    'GetCompanyLeasings': {
        'Participants': {
            'bool': 10
        },
        'Leasings': {
            'bool': [2, 3]
        }
    },
    'GetEntrepreneurLeasings': {
        'Participants': {
            'bool': 10
        },
        'Leasings': {
            'bool': [2, 3]
        }
    },
    'GetLeasingReport': {
        'Main': {
            'bool': [1, 2]
        },
        'Report': {
            'bool': 8
        }
    },
    'GetCompanySparkRisksReportXML': {
        'Main': {
            'bool': [11, 12, 46, 86],
            'float': [19, 97, 99, 111],
            'int': [
                58, 61, 63, 65, 90, 91,  92,
                93, 94, 95, 96, 98, 100, 101,
                102, 103, 104, 106, 107, 108,
                109, 110, 112, 113, 114, 115,
                116, 117, 118, 119, 120, 121,
                122, 123, 124, 125, 126, 127,
                128, 129, 130, 131, 132, 133,
                134, 135, 136, 137, 138, 139,
                140, 141, 142, 143
                ]
        },
        'ListName': {
            'bool': 3
        },
        'MainCoowners': {
            'float': 12
        },
        'TaxesFTS': {
            'float': [2, 3, 4]
        },
        'TaxesFTSDetail': {
            'float': 4
        },
        'Finance': {
            'float': 6
        }
    },

    # ================== 2 ==================
    'GetCompanyPledges': {
        'Main': {
            'bool': 6
        },
        'PledgesParticipants': {
            'bool': 8
        },
        'Pledges': {
            'bool': 2
        }
    },
    'GetEntrepreneurPledges': {
        'PledgesParticipants': {
            'bool': 8
        },
        'Pledges': {
            'bool': 2
        }
    },
    'GetPledgeReport': {
        'Main': {
            'bool': 1
        },
        'Pledges': {
            'bool': 8
        }
    },
    'GetCompanyExecutionProceedings': {
        'Main': {
            'bool': 6
        },
        'ExecutionProceedings': {
            'bool': 1,
            'float': 4
        }
    },
    'GetEntrepreneurExecutionProceedings': {
        'ExecutionProceedings': {
            'bool': 1,
            'float': 4
        }
    },
    'GetCompanyCounterparties': {
        'Main': {
            'bool': 6
        },
        'Counterparties': {
            'bool': 10
        }
    },

    # ================== 3 ==================
    'GetCompanyLicenses': {
        'Main': {
            'bool': 6
        }
    },
    'GetCompanyFinancialAnalysis': {
        'Main': {
            'bool': 6
        },
        'FinIndicators': {
            'float': [4, 5, 6, 7]
        }
    },
    'GetCompanyRiskFactors': {
        'Main': {
            'bool': 6,
            'float': [14, 16]
        }
    },
    'GetBankAccountingReport101102_101': {
        'Main': {
            'bool': 5
        },
        'Form101': {
            'float': [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        }
    },
    'GetBankAccountingReport101102_102': {
        'Main': {
            'bool': 5
        },
        'Form102': {
            'float': [2, 4, 5]
        }
    },
    'GetCompanyPaymentDiscipline': {
        'Main': {
            'bool': 6
        },
        'PaymentIndexValues': {
            'int': [2, 4]
        },
        'PaymentIndexDynamics': {
            'int': [3, 5, 6],
            'float': 7
        },
        'AnalysisByAmount': {
            'int': [3, 6, 7, 8, 11],
            'float': [4, 5, 9, 10]
        },
        'AnalysisByIndustry': {
            'int': [3, 8, 11],
            'float': [4, 5, 9, 10]
        },
        'Overdue': {
            'int': [2, 3, 5, 6, 7, 8]
        }
    },
    'GetCompanyAccountingReport': {
        'Main': {
            'bool': 5
        },
        'Period': {
            'int': 3,
            'float': 7
        }
    },
    'GetEntrepreneurShortReport': {
        'Main': {
            'bool': [1, 4],
            'int': [45, 46, 47, 48, 49, 50]
        },
        'OKVED2List': {
            'bool': 3
        },
        'PhoneList': {
            'bool': 4
        },
        'LinkedOGRNIP': {
            'bool': 2
        },
        'IncludeInList': {
            'bool': 2
        },
        'ArbitrationCases': {
            'float': [7, 10],
            'int': [1, 2, 3, 4, 5, 7, 9, 11]
        },
        'BankruptcyMessage': {
            'bool': 7
        },
        'StateContracts': {
            'float': 7,
            'int': [3, 4, 5, 6]
        }
    },
    'GetCompanyExtendedReport': {
        'Main': {
            'bool': [2, 5, 8, 10],
            'float': [36, 46, 48],
            'int': [
                1,  42, 76, 77,  78,  79,  80,
                81, 82, 83, 84,  85,  86,  89,
                90, 91, 92, 93,  94,  95,  96,
                97, 98, 99, 100, 101, 102, 103
            ]
        },
        'OKVED2List': {
            'bool': [3, 4, 5]
        },
        'CharterCapitalHistory': {
            'float': 2
        },
        'Addresses': {
            'bool': 17,
        },
        'PhoneList': {
            'bool': 6
        },
        'IncludeInList': {
            'bool': 2
        },
        'Finance': {
            'int': 1,
            'float': 9
        },
        'StateContracts': {
            'int': [3, 4, 5, 6],
            'float': 7
        },
        'ArbitrationCases': {
            'float': [8, 10],
            'int': [1, 2, 3, 4, 5, 7, 9, 11]
        },
        'FinanceAndTaxesFTS': {
            'float': [2, 3, 5, 8, 9, 10, 11]
        },
        'IncludeInList': {
            'bool': 2
        },
        'StaffNumberFTS': {
            'int': 2
        },
        'Coowners': {},
        'Branches': {},
        'BranchesEgrul': {}
    },
    'GetChangedCompanies': {
        'Main': {
            'bool': 3
        }
    },
    'GetChangedEntrepreneurs': {
        'Main': {
            'bool': 3
        }
    },

    # ================ 4 ===============
    'GetCompanyBeneficiariesAndAffiliates': {
        'Main': {
            'bool': [6,8]
        },
        'BeneficiariesAndAffiliates': {}
    },
    'GetOwnershipHierarchy': {
        'Main': {
            'bool': [9, 11]
        },
        'Coowners': {
            'float': [19, 20, 21]
        }
    },
    'GetCompanyStructure': {
        'Main': {
            'bool': [6, 8]
        },
        'Coowners': {
            'int': 4,
            'float': 20
        },
        'CoownerEGRUL_Pledge': {},
        'Branch': {},
        'AffiliatedCompanies': {
            'float': 7
        },
        'NonprofitOrganizationsRosstat': {}
    },
    'GetCompanyPredecessorSuccessor': {
        'Main': {
            'bool': 6
        },
        'Reorganizations': {
            'bool': [2, 9]
        }
    },
    'OrderCompanyBeneficiariesAndAffiliates': {
        'Main': {}
    }
}


PARQUET_SCHEMAS = {
    # ================== 1 ==================
    'GetCompanyArbitrationSummary': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string()),
            ('ArbitrationSummary_Total', pa.int64()),
            ('ArbitrationSummary_Considered', pa.int64()),
            ('ArbitrationSummary_Appealed', pa.int64()),
            ('ArbitrationSummary_DecisionsAndRulings', pa.int64()),
            ('ArbitrationSummary_Completed', pa.int64()),
            ('Plaintiff_Total', pa.int64()),
            ('Plaintiff_TotalSum', pa.float32()),
            ('Plaintiff_Considered', pa.int64()),
            ('Plaintiff_ConsideredSum', pa.float32()),
            ('Plaintiff_Appealed', pa.int64()),
            ('Plaintiff_AppealedSum', pa.float32()),
            ('Plaintiff_DecisionsAndRulings', pa.int64()),
            ('Plaintiff_DecisionsAndRulingsSum', pa.float32()),
            ('Plaintiff_Completed', pa.int64()),
            ('Plaintiff_CompletedSum', pa.float32()),
            ('Defendant_Total', pa.int64()),
            ('Defendant_TotalSum', pa.float32()),
            ('Defendant_Considered', pa.int64()),
            ('Defendant_ConsideredSum', pa.float32()),
            ('Defendant_Appealed', pa.int64()),
            ('Defendant_AppealedSum', pa.float32()),
            ('Defendant_DecisionsAndRulings', pa.int64()),
            ('Defendant_DecisionsAndRulingsSum', pa.float32()),
            ('Defendant_Completed', pa.int64()),
            ('Defendant_CompletedSum', pa.float32())
        ]),
        'FaceResult': pa.schema([
            ('SparkID', pa.string()),
            ('Face', pa.string()),
            ('Type_Result', pa.string()),
            ('Id', pa.string()),
            ('Name', pa.string()),
            ('CasesNumber', pa.int64()),
            ('Sum', pa.float32())
        ]),
        'ByType': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('Name', pa.string()),
            ('Plaintiff_Total', pa.int64()),
            ('Plaintiff_Considered', pa.int64()),
            ('Plaintiff_Appealed', pa.int64()),
            ('Plaintiff_Completed', pa.int64()),
            ('Defendant_Total', pa.int64()),
            ('Defendant_Considered', pa.int64()),
            ('Defendant_Appealed', pa.int64()),
            ('Defendant_Completed', pa.int64())
        ]),
        'ByYear': pa.schema([
            ('SparkID', pa.string()),
            ('Year', pa.string()),
            ('Plaintiff_CasesNumber', pa.int64()),
            ('Plaintiff_Sum', pa.float32()),
            ('Defendant_CasesNumber', pa.int64()),
            ('Defendant_Sum', pa.float32()),
            ('ThirdOrOtherPerson_CasesNumber', pa.int64())
        ])
    },
    'GetEntrepreneurArbitrationSummary': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRNIP', pa.string()),
            ('OKPO', pa.string()),
            ('ArbitrationSummary_Total', pa.int64()),
            ('ArbitrationSummary_Considered', pa.int64()),
            ('ArbitrationSummary_Appealed', pa.int64()),
            ('ArbitrationSummary_DecisionsAndRulings', pa.int64()),
            ('ArbitrationSummary_Completed', pa.int64()),
            ('Plaintiff_Total', pa.int64()),
            ('Plaintiff_TotalSum', pa.float32()),
            ('Plaintiff_Considered', pa.int64()),
            ('Plaintiff_ConsideredSum', pa.float32()),
            ('Plaintiff_Appealed', pa.int64()),
            ('Plaintiff_AppealedSum', pa.float32()),
            ('Plaintiff_DecisionsAndRulings', pa.int64()),
            ('Plaintiff_DecisionsAndRulingsSum', pa.float32()),
            ('Plaintiff_Completed', pa.int64()),
            ('Plaintiff_CompletedSum', pa.float32()),
            ('Defendant_Total', pa.int64()),
            ('Defendant_TotalSum', pa.float32()),
            ('Defendant_Considered', pa.int64()),
            ('Defendant_ConsideredSum', pa.float32()),
            ('Defendant_Appealed', pa.int64()),
            ('Defendant_AppealedSum', pa.float32()),
            ('Defendant_DecisionsAndRulings', pa.int64()),
            ('Defendant_DecisionsAndRulingsSum', pa.float32()),
            ('Defendant_Completed', pa.int64()),
            ('Defendant_CompletedSum', pa.float32())
        ]),
        'FaceResult': pa.schema([
            ('SparkID', pa.string()),
            ('Face', pa.string()),
            ('Type_Result', pa.string()),
            ('Id', pa.string()),
            ('Name', pa.string()),
            ('CasesNumber', pa.int64()),
            ('Sum', pa.float32())
        ]),
        'ByType': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('Name', pa.string()),
            ('Plaintiff_Total', pa.int64()),
            ('Plaintiff_Considered', pa.int64()),
            ('Plaintiff_Appealed', pa.int64()),
            ('Plaintiff_Completed', pa.int64()),
            ('Defendant_Total', pa.int64()),
            ('Defendant_Considered', pa.int64()),
            ('Defendant_Appealed', pa.int64()),
            ('Defendant_Completed', pa.int64())
        ]),
        'ByYear': pa.schema([
            ('SparkID', pa.string()),
            ('Year', pa.string()),
            ('Plaintiff_CasesNumber', pa.int64()),
            ('Plaintiff_Sum', pa.float32()),
            ('Defendant_CasesNumber', pa.int64()),
            ('Defendant_Sum', pa.float32()),
            ('ThirdOrOtherPerson_CasesNumber', pa.int64())
        ])
    },
    'GetCompanyLeasings': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('FullName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string())
        ]),
        'Participants': pa.schema([
            ('SparkID', pa.string()),
            ('ID', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('Participant_SparkID', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('BirthDate', pa.string()),
            ('Code', pa.string()),
            ('Date', pa.string()),
            ('IsActing', pa.int8()),
            ('Text', pa.string())
        ]),
        'Leasings': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('IsActing', pa.int8()),
            ('IsSublease', pa.int8()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('StartDate', pa.string()),
            ('EndDate', pa.string()),
            ('StopReason', pa.string()),
            ('StopReason_Date', pa.string()),
            ('Lessors_Id', pa.string()),
            ('Lessees_Id', pa.string()),
            ('ItemsNumber', pa.string()),
            ('PropertyType', pa.string()),
            ('Code', pa.string())
        ])
    },
    'GetEntrepreneurLeasings': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('FullName', pa.string()),
            ('INN', pa.string()),
            ('OGRNIP', pa.string()),
            ('OKPO', pa.string())
        ]),
        'Participants': pa.schema([
            ('SparkID', pa.string()),
            ('ID', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('Participant_SparkID', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('BirthDate', pa.string()),
            ('Code', pa.string()),
            ('Date', pa.string()),
            ('IsActing', pa.int8()),
            ('Text', pa.string())
        ]),
        'Leasings': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('IsActing', pa.int8()),
            ('IsSublease', pa.int8()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('StartDate', pa.string()),
            ('EndDate', pa.string()),
            ('StopReason', pa.string()),
            ('StopReason_Date', pa.string()),
            ('Lessors_Id', pa.string()),
            ('Lessees_Id', pa.string()),
            ('ItemsNumber', pa.string()),
            ('PropertyType', pa.string()),
            ('Code', pa.string())
        ])
    },
    'GetLeasingReport': {
        'Main': pa.schema([
            ('Leasing_Id', pa.string()),
            ('IsActing', pa.int8()),
            ('IsSublease', pa.int8()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('StartDate', pa.string()),
            ('EndDate', pa.string()),
            ('StopReason', pa.string()),
            ('Date', pa.string()),
            ('Number', pa.string()),
            ('MainConctract_Date', pa.string())
        ]),
        'Report': pa.schema([
            ('Leasing_Id', pa.string()),
            ('Face', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('Lessors_SparkID', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('BirthDate', pa.string()),
            ('IsActing', pa.int8()),
            ('Code', pa.string()),
            ('Text', pa.string()),
            ('Date', pa.string())
        ]),
        'Items': pa.schema([
            ('Leasing_Id', pa.string()),
            ('Id', pa.string()),
            ('TypeCode', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string())
        ])
    },
    'GetCompanySparkRisksReportXML': {
        'Main': pa.schema([
            ('SparkID', pa.string()), # 0
            ('ShortName', pa.string()),
            ('FullName', pa.string()),
            ('INN', pa.string()),
            ('KPP', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKFS_Code', pa.string()),
            ('OKFS_Name', pa.string()),
            ('OKVED_Code', pa.string()),
            ('OKVED_Name', pa.string()), # 10
            ('OKVED_IsMain', pa.int8()),
            ('IsActing', pa.int8()),
            ('Code', pa.string()),
            ('Text', pa.string()),
            ('GroupID', pa.string()),
            ('GroupName', pa.string()),
            ('Date', pa.string()),
            ('DateFirstReg', pa.string()),
            ('CharterCapital', pa.float32()),
            ('ActualDate', pa.string()), # 20
            ('ActualDate_Leader', pa.string()),
            ('FIO_Leader', pa.string()),
            ('Position_Leader', pa.string()),
            ('INN_Leader', pa.string()),
            ('LegalCapacityEndDate', pa.string()),
            ('ManagmentCompany', pa.string()),
            ('ManagmentCompanyINN', pa.string()),
            ('PostCode', pa.string()),
            ('Address', pa.string()),
            ('Region', pa.string()), # 30
            ('Rayon', pa.string()),
            ('City', pa.string()),
            ('StreetName', pa.string()),
            ('BuildingType', pa.string()),
            ('BuildingNumber', pa.string()),
            ('HousingType', pa.string()),
            ('Housing', pa.string()),
            ('BlockType', pa.string()),
            ('Block', pa.string()),
            ('RoomType', pa.string()), # 40
            ('Room', pa.string()),
            ('Longited', pa.string()),
            ('Latitude', pa.string()),
            ('BusinnesCenterName', pa.string()),
            ('FiasGUID', pa.string()),
            ('IsHouseFiasGUID', pa.int8()),
            ('FiasCode', pa.string()),
            ('FiasRegion', pa.string()),
            ('FiasArea', pa.string()),
            ('FIasCity', pa.string()), # 50
            ('FiasPlace', pa.string()),
            ('FiasPlan', pa.string()),
            ('FiasStreet', pa.string()),
            ('ActualDate_LegalAddress', pa.string()),
            ('Sites', pa.string()),
            ('Emails', pa.string()),
            ('WorkersRange', pa.string()),
            ('VacanciesNumber', pa.int64()),
            ('Value_ConsolidatedIndicator', pa.string()),
            ('Description', pa.string()), # 60
            ('Index', pa.int64()),
            ('IndexDesc', pa.string()),
            ('FailureScoreValue', pa.int64()),
            ('FailureScoreDesc', pa.string()),
            ('PaymentIndexValue', pa.int64()),
            ('PaymentIndexDesc', pa.string()),
            ('SparkID_Registrar', pa.string()),
            ('Name_Registrar', pa.string()),
            ('INN_Registrar', pa.string()),
            ('OGRN_Registrar', pa.string()), # 70
            ('ContractEndDate', pa.string()),
            ('SparkID_HeadOfCompany', pa.string()),
            ('Name_HeadOfCompany', pa.string()),
            ('INN_HeadOfCompany', pa.string()),
            ('OGRN_HeadOfCompany', pa.string()),
            ('Country_Code', pa.string()),
            ('Country_Name', pa.string()),
            ('FIO_Beneficiary', pa.string()),
            ('INN_Beneficiary', pa.string()),
            ('SparkID_Successor', pa.string()), # 80
            ('Name_Successor', pa.string()),
            ('Address_Successor', pa.string()),
            ('INN_Successor', pa.string()),
            ('ORGN_Successor', pa.string()),
            ('FullName_Successor', pa.string()),
            ('IsActing_Status', pa.int8()),
            ('Text_Status', pa.string()),
            ('Code_Status', pa.string()),
            ('Date_State', pa.string()),
            ('Total', pa.int64()), # 90
            ('Considered', pa.int64()),
            ('Appealed', pa.int64()),
            ('DecisionsAndRulings', pa.int64()),
            ('Completed', pa.int64()),
            ('WonNumber', pa.int64()),
            ('Active', pa.int64()),
            ('ActiveSum', pa.float32()),
            ('Executed',  pa.int64()),
            ('ExecutedSum', pa.float32()),
            ('CompletedNoLocation', pa.int64()), # 100
            ('CompletedNoProperty', pa.int64()),
            ('CompletedOther', pa.int64()),
            ('TrafficFines', pa.int64()),
            ('ActiveBranchesRosstatNumber', pa.int64()),
            ('ActiveAffiliatedCompaniesNumber_Source', pa.string()),
            ('ActiveAffiliatedCompaniesNumber', pa.int64()),
            ('AdmittedNumber', pa.int64()),
            ('NotAdmittedNumber', pa.int64()),
            ('WinnerNumber', pa.int64()),
            ('SignedNumber', pa.int64()), # 110
            ('Sum_Contracts', pa.float32()),
            ('Active_Pledger', pa.int64()),
            ('Ceased_Pledger', pa.int64()),
            ('Active_Lessee', pa.int64()),
            ('Ceased_Lessee', pa.int64()),
            ('MortgagePropertiesNumber', pa.int64()),
            ('Number_Payments', pa.int64()),
            ('PayeesNumber', pa.int64()),
            ('CashRegistersNumber', pa.int64()),
            ('SalesPointsNumber', pa.int64()),
            ('SubsidiesSum', pa.int64()),
            ('ActiveLicensesNumber', pa.int64()),
            ('ActiveTaxiPermitsNumber', pa.int64()),
            ('ActiveCertificatesNumber', pa.int64()),
            ('RealPropertiesNumber', pa.int64()),
            ('RentalPropertiesNumber', pa.int64()),
            ('CustomsWarehousesNumber', pa.int64()),
            ('DutyFreeShopsNumber', pa.int64()),
            ('DomainsNumber', pa.int64()),
            ('TrademarksNumber', pa.int64()),
            ('InventionsNumber', pa.int64()),
            ('IndustrialModelsNumber', pa.int64()),
            ('ApplicationSoftwareNumber', pa.int64()),
            ('IntegratedCircuitTopographiesNumber', pa.int64()),
            ('PatentApplicationNumber', pa.int64()),
            ('UsingTrademarksNumber', pa.int64()),
            ('ForestAreasNumber', pa.int64()),
            ('WaterBodiesNumber', pa.int64()),
            ('WoodDealsNumber', pa.int64()),
            ('TotalNumber', pa.int64()),
            ('Completed_Inspections', pa.int64()),
            ('WithViolations', pa.int64()),
            ('Scheduled', pa.int64())
        ]),
        'Phones': pa.schema([
            ('SparkID', pa.string()),
            ('Code', pa.string()),
            ('Number', pa.string()),
            ('Status', pa.string()),
            ('VerificationDate', pa.string())
        ]),
        'ListName': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('ListName', pa.string()),
            ('IsNegative', pa.int64())
        ]),
        'AddInfo': pa.schema([ 
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('Type', pa.string()),
            ('AddField', pa.string()),
            ('Name', pa.string())
        ]),
        'Factor': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('Name', pa.string())
        ]),
        'Auditors': pa.schema([
            ('SparkID', pa.string()),
            ('SparkID_Auditor', pa.string()),
            ('Name', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('ContractYears', pa.string())
        ]),
        'FrozenAccounts': pa.schema([
            ('SparkID', pa.string()),
            ('Number', pa.string()),
            ('Date', pa.string()),
            ('Code', pa.string()),
            ('Name', pa.string()),
            ('BIK', pa.string()),
            ('SparkID_Bank', pa.string()),
            ('Name_Bank', pa.string())
        ]),
        'MainCoowners': pa.schema([
            ('SparkId', pa.string()),
            ('SparkId_Coowner', pa.string()),
            ('Name', pa.string()),
            ('Address', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKOPFName', pa.string()),
            ('Manager', pa.string()),
            ('ManagerInn', pa.string()),
            ('FullName', pa.string()),
            ('OKATO', pa.string()),
            ('SharePart', pa.float32())
        ]),
        'TaxesFTS': pa.schema([
            ('SparkId', pa.string()),
            ('EndDate', pa.string()),
            ('Income', pa.float32()),
            ('Expenses', pa.float32()),
            ('SumTaxes', pa.float32())
        ]),
        'TaxesFTSDetail': pa.schema([
            ('SparkId', pa.string()),
            ('EndDate', pa.string()),
            ('TaxId', pa.string()),
            ('TaxName', pa.string()),
            ('TaxSum', pa.float32())
        ]),
        'Finance': pa.schema([
            ('SparkId', pa.string()),
            ('BalanceType', pa.string()),
            ('PeriodName', pa.string()),
            ('DateBegin', pa.string()),
            ('DateEnd', pa.string()),
            ('Name', pa.string()),
            ('Value', pa.float32()),
            ('IdFinPok', pa.string())
        ]),
        'SROs': pa.schema([
            ('SparkId', pa.string()),
            ('SparkID_SRO', pa.string()),
            ('Name', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string())
        ])
    },

    # ================== 2 ==================
    'GetCompanyPledges': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('IsActing', pa.int8()),
            ('Code', pa.string()),
            ('Text', pa.string()),
            ('Date', pa.string())
        ]),
        'PledgesParticipants': pa.schema([
            ('SparkID', pa.string()),
            ('Participant_Id', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('Pledges_SparkID', pa.string()),
            ('Pledges_INN', pa.string()),
            ('Pledges_OGRN', pa.string()),
            ('BitrthDate', pa.string()),
            ('IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'Pledges': pa.schema([
            ('SparkID', pa.string()),
            ('Pledge_Id', pa.string()),
            ('IsActing', pa.int8()),
            ('NotificationNumber', pa.string()),
            ('NotificationDate', pa.string()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('PerfomanceDate', pa.string()),
            ('Date', pa.string()),
            ('StopReason', pa.string()),
            ('Pledgers', pa.string()),
            ('Pledgees', pa.string()),
            ('Code', pa.string()),
            ('PropertyType', pa.string())
        ])
    },
    'GetEntrepreneurPledges': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('FullName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string())
        ]),
        'PledgesParticipants': pa.schema([
            ('SparkID', pa.string()),
            ('Participant_Id', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('Pledges_SparkID', pa.string()),
            ('Pledges_INN', pa.string()),
            ('Pledges_OGRN', pa.string()),
            ('BirthDate', pa.string()),
            ('IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'Pledges': pa.schema([
            ('SparkID', pa.string()),
            ('Pledge_Id', pa.string()),
            ('IsActing', pa.int8()),
            ('NotificationNumber', pa.string()),
            ('NotificationDate', pa.string()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('PerfomanceDate', pa.string()),
            ('Date', pa.string()),
            ('StopReason', pa.string()),
            ('Pledgers', pa.string()),
            ('Pledgees', pa.string()),
            ('Code', pa.string()),
            ('PropertyType', pa.string())
        ])
    },
    'GetPledgeReport': {
        'Main': pa.schema([
            ('Id', pa.string()),
            ('IsActing', pa.int8()),
            ('NotificationNumber', pa.string()),
            ('NotificationDate', pa.string()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('PerformanceDate', pa.string()),
            ('StopReason_Date', pa.string()),
            ('StopReason', pa.string())
        ]),
        'Pledges': pa.schema([
            ('Face', pa.string()),
            ('Pledge_Id', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('SparkID_Face', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('BirthDate', pa.string()),
            ('IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'Items': pa.schema([
            ('Pledge_Id', pa.string()),
            ('TypeCode', pa.string()),
            ('Type', pa.string()),
            ('Item', pa.string())
        ])
    },
    'GetCompanyExecutionProceedings': {
        'Main': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ShortName', pa.string()),
                ('INN', pa.string()),
                ('OGRN', pa.string()),
                ('OKPO', pa.string()),
                ('OKATO', pa.string()),
                ('IsActing', pa.int8()),
                ('Status_Code', pa.string()),
                ('Status_Text', pa.string()),
                ('Status_Date', pa.string())
            ]),
        'ExecutionProceedings': pa.schema(
            [
                ('SparkID', pa.string()),
                ('IsExecuted', pa.int8()),
                ('Number', pa.string()),
                ('Date', pa.string()),
                ('PayoutAmount', pa.float32()),
                ('Department', pa.string()),
                ('Document', pa.string()),
                ('GroupId', pa.string()),
                ('GroupName', pa.string()),
                ('Type_Id', pa.string()),
                ('Type', pa.string()),
                ('Reason_Id', pa.string()),
                ('Name', pa.string()),
                ('Reason_Date', pa.string())
            ])
    },
    'GetEntrepreneurExecutionProceedings': {
        'Main': pa.schema(
            [
                ('SparkID', pa.string()),
                ('FullName', pa.string()),
                ('INN', pa.string()),
                ('OGRNIP', pa.string()),
                ('OKPO', pa.string())
            ]),
        'ExecutionProceedings': pa.schema(
            [
                ('SparkID', pa.string()),
                ('IsExecuted', pa.int8()),
                ('Number', pa.string()),
                ('Date', pa.string()),
                ('PayoutAmount', pa.float32()),
                ('Department', pa.string()),
                ('Document', pa.string()),
                ('GroupId', pa.string()),
                ('GroupName', pa.string()),
                ('Type_Id', pa.string()),
                ('Type', pa.string()),
                ('Reason_Id', pa.string()),
                ('Name', pa.string()),
                ('Reason_Date', pa.string())
            ])
    },
    'GetCompanyCounterparties': {
        'Main': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ShortName', pa.string()),
                ('INN', pa.string()),
                ('OGRN', pa.string()),
                ('OKPO', pa.string()),
                ('OKATO', pa.string()),
                ('IsActing', pa.int8()),
                ('Status_Code', pa.string()),
                ('Status_Text', pa.string()),
                ('Status_Date', pa.string())
            ]),
        'Counterparties': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('Name', pa.string()),
                ('Counterparty_SparkID', pa.string()),
                ('INN', pa.string()),
                ('OGRN', pa.string()),
                ('OKATO_Code', pa.string()),
                ('OKATO_RegionName', pa.string()),
                ('OKATO_RegionCode', pa.string()),
                ('Address', pa.string()),
                ('IsActing', pa.int8()),
                ('Status_Code', pa.string()),
                ('Status_Text', pa.string()),
                ('Status_Date', pa.string())
            ]),
        'Sources': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Counterparty_SparkID', pa.string()),
                ('Id', pa.string()),
                ('Name', pa.string())
            ])
    },

    # ================== 3 ==================
    'GetCompanyLicenses': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('EGRPOIncluded', pa.int8()),
            ('EGRULLikvidation', pa.string())
        ]),
        'Licenses': pa.schema([
            ('SparkID', pa.string()),
            ('Number', pa.string()),
            ('IssueDate', pa.string()),
            ('EndDate', pa.string()),
            ('ActivityKind', pa.string()),
            ('IssuingAuthority', pa.string()),
            ('CurrentStatus', pa.string()),
            ('StatusChangeLastDate', pa.string())
        ])
    },
    'GetCompanyFinancialAnalysis': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_GroupId', pa.string()),
            ('Status_GroupName', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'FinancialAnalysis': pa.schema([
            ('SparkID', pa.string()),
            ('PeriodName', pa.string()),
            ('DateBegin', pa.string()),
            ('DateEnd', pa.string()),
            ('Code', pa.string()),
            ('Name', pa.string())
        ]),
        'FinIndicators': pa.schema([
            ('SparkID', pa.string()),
            ('PeriodName', pa.string()),
            ('IdFinPok', pa.string()),
            ('Name', pa.string()),
            ('Value', pa.float64()),
            ('MedianValueByIndustry', pa.float64()),
            ('AbsoluteDeviation', pa.float64()),
            ('RelativeDeviation', pa.float64())
        ])
    },
    'GetCompanyRiskFactors': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_GroupId', pa.string()),
            ('Status_GroupName', pa.string()),
            ('Status_Date', pa.string()),
            ('Index', pa.string()),
            ('IndexDesc', pa.string()),
            ('FailureScoreValue', pa.float64()),
            ('FailureScoreDesc', pa.string()),
            ('PaymentIndexValue', pa.float64()),
            ('PaymentIndexDesc', pa.string())
        ]),
        'ConsolidatedIndicator': pa.schema([
            ('SparkID', pa.string()),
            ('ConsolidatedIndicator_Value', pa.string()),
            ('Description', pa.string()),
            ('Name', pa.string()),
            ('Value', pa.string()),
        ]),
        'RiskFactors': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('Factor_Name', pa.string()),
            ('Name', pa.string()),
            ('Value', pa.string()),
        ])
    },
    'GetBankAccountingReport101102_101': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('EGRPOIncluded', pa.int8())
        ]),
        'Form101': pa.schema([
            ('SparkID', pa.string()),
            ('DateEnd', pa.string()),
            ('Power_Form', pa.float32()),
            ('Order', pa.string()),
            ('Inpartrub', pa.float32()),
            ('Inpartival', pa.float32()),
            ('Inparttotal', pa.float32()),
            ('Oborotactivrub', pa.float32()),
            ('Oborotaktivval', pa.float32()),
            ('Oborotaktivtotal', pa.float32()),
            ('Oborotpassivrub', pa.float32()),
            ('Oborotpassivval', pa.float32()),
            ('Oborotpassivtotal', pa.float32()),
            ('Outpartrub', pa.float32()),
            ('Outpartval', pa.float32()),
            ('Outparttotal', pa.float32())
        ])
    },
    'GetBankAccountingReport101102_102': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('EGRPOIncluded', pa.int8())
        ]),
        'Form102': pa.schema([
            ('SparkID', pa.string()),
            ('DateEnd', pa.string()),
            ('Power_Form', pa.float32()),
            ('Clausename', pa.string()),
            ('Numberofclause', pa.string()),
            ('Valuetotal', pa.float64())
        ])
    },
    'GetCompanyPaymentDiscipline': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'PaymentIndexValues': pa.schema([
            ('SparkID', pa.string()),
            ('Name', pa.string()),
            ('Value', pa.int64()),
            ('Description', pa.string()),
            ('AverageOverdue', pa.int64())
        ]),
        'PaymentIndexDynamics': pa.schema([
            ('SparkID', pa.string()),
            ('StartDate', pa.string()),
            ('EndDate', pa.string()),
            ('Value', pa.int64()),
            ('Description', pa.string()),
            ('CounterpartiesNumber', pa.int64()),
            ('InvoicesNumber', pa.int64()),
            ('Sum', pa.float32())
        ]),
        'AnalysisByAmount': pa.schema([
            ('SparkID', pa.string()),
            ('StartDate', pa.string()),
            ('EndDate', pa.string()),
            ('InvoicesAnalysis_InvoicesNumber', pa.int64()),
            ('InvoicesAnalysis_PaidSum', pa.float64()),
            ('InvoicesAnalysis_DebtSum', pa.float64()),
            ('MinValue', pa.int64()),
            ('MaxValue', pa.int64()),
            ('AmountRange_InvoicesNumber', pa.int64()),
            ('AmountRange_PaidSum', pa.float64()),
            ('AmountRange_DebtSum', pa.float64()),
            ('AmountRange_PaidOnTime', pa.int64())
        ]),
        'AnalysisByIndustry': pa.schema([
            ('SparkID', pa.string()),
            ('StartDate', pa.string()),
            ('EndDate', pa.string()),
            ('InvoicesAnalysis_InvoicesNumber', pa.int64()),
            ('InvoicesAnalysis_PaidSum', pa.float64()),
            ('InvoicesAnalysis_DebtSum', pa.float64()),
            ('Id', pa.string()),
            ('Name', pa.string()),
            ('InvoicesNumber', pa.int64()),
            ('PaidSum', pa.float64()),
            ('DebtSum', pa.float64()),
            ('PaidOnTime', pa.int64())
        ]),
        'Overdue': pa.schema([
            ('SparkID', pa.string()),
            ('Type', pa.string()),
            ('AnalysisByAmount_MinValue', pa.int64()),
            ('AnalysisByAmount_MaxValue', pa.int64()),
            ('Id', pa.string()),
            ('InvoicesNumber', pa.string()),
            ('MinValue', pa.int64()),
            ('MaxValue', pa.int64()),
            ('InvoicesPercent', pa.int64())
        ])
    },
    'GetCompanyAccountingReport': {
        'Main': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ShortName', pa.string()),
                ('INN', pa.string()),
                ('OGRN', pa.string()),
                ('OKPO', pa.string()),
                ('EGRPOIncluded', pa.int8()),
                ('EGRULLikvidation', pa.string()),
                ('PeriodName', pa.string()),
                ('DateBegin', pa.string()),
                ('DateEnd', pa.string()),
                ('OKVEDCode', pa.string()),
                ('ReportType', pa.string())
            ]),
        'Period': pa.schema(
            [
                ('SparkID', pa.string()),
                ('PeriodName', pa.string()),
                ('ID', pa.string()),
                ('Power', pa.int64()),
                ('Code', pa.string()),
                ('Name', pa.string()),
                ('Column', pa.string()),
                ('Value', pa.float64())
            ])
    },
    'GetEntrepreneurShortReport': {
        'Main': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Status_IsActing', pa.int8()),
                ('Status_Code', pa.string()),
                ('Status_Text', pa.string()),
                ('Status_GroupId', pa.int8()),
                ('Status_GroupName', pa.string()),
                ('Status_Date', pa.string()),
                ('DateFirstReg', pa.string()),
                ('DateReg', pa.string()),
                ('FullNameRus', pa.string()),
                ('INN', pa.string()),
                ('OGRNIP', pa.string()),
                ('OKPO', pa.string()),
                ('OKATO_Code', pa.string()),
                ('OKATO_RegionName', pa.string()),
                ('OKATO_RegionCode', pa.string()),
                ('OKTMO_Code', pa.string()),
                ('OKOPF_Code', pa.string()),
                ('OKOPF_Name', pa.string()),
                ('PaymentIndexValue', pa.string()),
                ('PaymentIndexDesc', pa.string()),
                ('FederalTaxRegistration_RegDate', pa.string()),
                ('FederalTaxRegistration_RegAuthority', pa.string()),
                ('FederalTaxRegistration_RegAuthorityAddress', pa.string()),
                ('FederalTaxRegistration_RegAuthorityCode', pa.string()),
                ('FederalTaxRegistrationCurrent_RegDate', pa.string()),
                ('FederalTaxRegistrationCurrent_RegAuthority', pa.string()),
                ('FederalTaxRegistrationCurrent_RegAuthorityAddress', pa.string()),
                ('FederalTaxRegistrationCurrent_RegAuthorityCode', pa.string()),
                ('FederalTaxRegistrationPayment_RegDate', pa.string()),
                ('FederalTaxRegistrationPayment_RegAuthority', pa.string()),
                ('FederalTaxRegistrationPayment_RegAuthorityAddress', pa.string()),
                ('FederalTaxRegistrationPayment_RegAuthorityCode', pa.string()),
                ('PensionFund_RegistrationDate', pa.string()),
                ('PensionFund_DeregistrationDate', pa.string()),
                ('PensionFund_RegisterNumber', pa.string()),
                ('PensionFund_RegAuthority', pa.string()),
                ('SocialInsuranceFund_RegistrationDate', pa.string()),
                ('SocialInsuranceFund_DeregistrationDate', pa.string()),
                ('SocialInsuranceFund_RegisterNumber', pa.string()),
                ('SocialInsuranceFund_RegAuthority', pa.string()),
                ('BirthDate', pa.string()),
                ('BirthPlace', pa.string()),
                ('Sex_Code', pa.string()),
                ('Sex_Name', pa.string()),
                ('Citizenship_Code', pa.string()),
                ('Citizenship_Name', pa.string()),
                ('ExecutionProceedings_Active', pa.int64()),
                ('ExecutionProceedings_Executed', pa.int64()),
                ('Pledger_Active', pa.int64()),
                ('Pledger_Ceased', pa.int64()),
                ('Pledgee_Active', pa.int64()),
                ('Pledgee_Ceased', pa.int64())
            ]
        ),
        'OKVED2List': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Code', pa.string()),
                ('Name', pa.string()),
                ('IsMain', pa.int8())
            ]
        ),

        'PhoneList': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Code', pa.string()),
                ('Number', pa.string()),
                ('Status', pa.string()),
                ('IsOpenData', pa.int8())
            ]
        ),
        'SubmittedStatements': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Form', pa.string()),
                ('ReferenceNumber', pa.string()),
                ('SubmissionDate', pa.string()),
                ('AvailabilityDate', pa.string()),
                ('GRN', pa.string()),
                ('DecisionType', pa.string())
            ]
        ),
        'RegistrationCertificates': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Series', pa.string()),
                ('Number', pa.string()),
                ('IssueDate', pa.string()),
                ('GRN', pa.string())
            ]
        ),
        'LinkedOGRNIP': pa.schema(
            [
                ('SparkID', pa.string()),
                ('OGRNIP', pa.string()),
                ('IsActing', pa.int8())
            ]
        ),
        'Licenses': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Number', pa.string()),
                ('IssueDate', pa.string()),
                ('EndDate', pa.string()),
                ('ActivityKind', pa.string()),
                ('IssuingAuthority', pa.string())
            ]
        ),
        'IncludeInList': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('IsNegative', pa.int8()),
                ('ListName', pa.string())
            ]
        ),
        'IncludeInList_AddInfo': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Name', pa.string()),
                ('TextField', pa.string())
            ]
        ),

        'Disqualifications': pa.schema(
            [
                ('SparkID', pa.string()),
                ('RegisterNumber', pa.string()),
                ('Article', pa.string()),
                ('StartDate', pa.string()),
                ('EndDate', pa.string()),
                ('Period', pa.string()),
                ('DisqualifiedInCompany', pa.string())
            ]
        ),
        'ArbitrationCases': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Total', pa.int64()),
                ('Considered', pa.int64()),
                ('Appealed', pa.int64()),
                ('DecisionsAndRulings', pa.int64()),
                ('Completed', pa.int64()),
                ('Year', pa.string()),
                ('Plaintiff_CasesNumber', pa.int64()),
                ('Plaintiff_Sum', pa.float32()),
                ('Defendant_CasesNumber', pa.int64()),
                ('Defendant_Sum', pa.float32()),
                ('ThirdOrOtherPerson_CasesNumber', pa.int64())
            ]
        ),
        'ArbitrationCases_Year': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Year', pa.string()),
                ('Plaintiff_CasesNumber', pa.string()),
                ('Plaintiff_Sum', pa.string()),
                ('Defendant_CasesNumber', pa.string()),
                ('Defendant_Sum', pa.string()),
                ('ThirdOrOtherPerson_CasesNumber', pa.string())
            ]
        ),
        'FrozenAccounts': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Decision_Number', pa.string()),
                ('Decision_Date', pa.string()),
                ('Reason_Id', pa.string()),
                ('Reason_Name', pa.string()),
                ('TaxAuthority_Code', pa.string()),
                ('TaxAuthority_Name', pa.string()),
                ('Bank_BIK', pa.string()),
                ('Bank_SparkID', pa.string()),
                ('Bank_Name', pa.string()),
            ]
        ),
        'BankruptcyMessage': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Date', pa.string()),
                ('DecisionDate', pa.string()),
                ('IdType', pa.string()),
                ('Type', pa.string()),
                ('CanceledMessageId', pa.string()),
                ('IsCanceled', pa.int8()),
                ('CaseId', pa.string()),
                ('CaseNumber', pa.string())
            ]
        ),
        'BankruptcyArbitrationCases': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Number', pa.string()),
                ('StatusId', pa.string()),
                ('StatusName', pa.string()),
                ('RegistrationDate', pa.string()),
                ('AcceptanceDate', pa.string()),
                ('SupervisionDate', pa.string()),
                ('FinancialRecoveryDate', pa.string()),
                ('ExternalManagementDate', pa.string()),
                ('BankruptcyProceedingsDate', pa.string()),
                ('CompleteDate', pa.string())
            ]
        ),
        'StateContracts': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('Year', pa.string()),
                ('AdmittedNumber', pa.int64()),
                ('NotAdmittedNumber', pa.int64()),
                ('WinnerNumber', pa.int64()),
                ('SignedNumber', pa.int64()),
                ('Sum', pa.float64())
            ]
        )
    },
    'GetCompanyExtendedReport': {
        'Main': pa.schema(
            [
                ('SparkID', pa.string()),
                ('CompanyType', pa.int64()),
                ('Status_IsActing', pa.int8()),
                ('Status_Code', pa.string()),
                ('Status_Type', pa.string()),
                ('Status_GroupId', pa.int64()),
                ('Status_GroupName', pa.string()),
                ('Status_Date', pa.string()),
                ('EGRPOIncluded', pa.int64()),
                ('EGRULLikvidation', pa.string()),
                ('IsActing', pa.int8()),
                ('DateFirstReg', pa.string()),
                ('ShortName', pa.string()),
                ('ShortNameRus', pa.string()),
                ('ShortNameEn', pa.string()),
                ('FullNameRus', pa.string()),
                ('NormName', pa.string()),
                ('GUID', pa.string()),
                ('INN', pa.string()),
                ('KPP', pa.string()),
                ('OGRN', pa.string()),
                ('OKPO', pa.string()),
                ('BIK', pa.string()),
                ('FCSMCode', pa.string()),
                ('RTS', pa.string()),
                ('OKATO_Code', pa.string()),
                ('OKATO_RegionName', pa.string()),
                ('OKATO_RegionCode', pa.string()),
                ('OKTMO_Code', pa.string()),
                ('OKOGU_Code', pa.string()),
                ('OKOGU_Name', pa.string()),
                ('OKFS_Code', pa.string()),
                ('OKFS_Name', pa.string()),
                ('OKOPF_Code', pa.string()),
                ('OKOPF_CodeNew', pa.string()),
                ('OKOPF_Name', pa.string()),
                ('CharterCapital', pa.float64()),
                ('Email', pa.string()),
                ('Www', pa.string()),
                ('WorkersRange', pa.string()),
                ('Index', pa.string()),
                ('IndexDesc', pa.string()),
                ('FailureScoreValue', pa.int64()),
                ('FailureScoreDesc', pa.string()),
                ('PaymentIndexValue', pa.string()),
                ('PaymentIndexDesc', pa.string()),
                ('CreditLimit_Value', pa.float64()),
                ('CreditLimit_Description', pa.string()),
                ('CompanySize_Revenue', pa.float64()),
                ('CompanySize_Description', pa.string()),
                ('CompanySize_ActualDate', pa.string()),
                ('FederalTaxRegistration_RegDate', pa.string()),
                ('FederalTaxRegistration_RegAuthority', pa.string()),
                ('FederalTaxRegistration_RegAuthorityAddress', pa.string()),
                ('FederalTaxRegistration_RegAuthorityCode', pa.string()),
                ('FederalTaxRegistrationCurrent_RegDate', pa.string()),
                ('FederalTaxRegistrationCurrent_RegAuthority', pa.string()),
                ('FederalTaxRegistrationCurrent_RegAuthorityAddress', pa.string()),
                ('FederalTaxRegistrationCurrent_RegAuthorityCode', pa.string()),
                ('FederalTaxRegistrationPayment_RegDate', pa.string()),
                ('FederalTaxRegistrationPayment_RegAuthority', pa.string()),
                ('FederalTaxRegistrationPayment_RegAuthorityAddress', pa.string()),
                ('FederalTaxRegistrationPayment_RegAuthorityCode', pa.string()),
                ('RegisterNumber', pa.string()),
                ('PensionFund_RegistrationDate', pa.string()),
                ('PensionFund_DeregistrationDate', pa.string()),
                ('PensionFund_RegisterNumber', pa.string()),
                ('PensionFund_RegAuthority', pa.string()),
                ('SocialInsuranceFund_RegistrationDate', pa.string()),
                ('SocialInsuranceFund_DeregistrationDate', pa.string()),
                ('SocialInsuranceFund_RegisterNumber', pa.string()),
                ('SocialInsuranceFund_RegAuthority', pa.string()),
                ('CompulsoryMedicalInsuranceFund_RegistrationDate', pa.string()),
                ('CompulsoryMedicalInsuranceFund_DeregistrationDate', pa.string()),
                ('CompulsoryMedicalInsuranceFund_RegisterNumber', pa.string()),
                ('CompulsoryMedicalInsuranceFund_RegAuthority', pa.string()),
                ('CountCoownerFCSM', pa.int64()),
                ('CountCoownerRosstat', pa.int64()),
                ('CountCoownerEGRUL', pa.int64()),
                ('CountBranch', pa.int64()),
                ('CountBranchRosstat', pa.int64()),
                ('CountBranchEGRUL', pa.int64()),
                ('CountAffiliatedCompanyFCSM', pa.int64()),
                ('CountAffiliatedCompanyRosstat', pa.int64()),
                ('CountAffiliatedCompanyEGRUL', pa.int64()),
                ('NonprofitOrganizationRosstat', pa.int64()),
                ('TelephoneCount', pa.int64()),
                ('PhoneCode', pa.string()),
                ('PhoneNumber', pa.string()),
                ('CompanyWithSameInfo_AddressCount', pa.int64()),
                ('CompanyWithSameInfo_AddressWithoutRoomCount', pa.int64()),
                ('AddressNotAffiliatedCount', pa.int64()),
                ('AddressFTSCount', pa.int64()),
                ('ManagerCountInCountry', pa.int64()),
                ('ManagerCountInRegion', pa.int64()),
                ('ManagerInnCount', pa.int64()),
                ('CompanyLiquidatedWithSameInfo_AddressCount', pa.int64()),
                ('CompanyLiquidatedWithSameInfo_AddressWithoutRoomCount', pa.int64()),
                ('ExecutionProceedings_Active', pa.int64()),
                ('ExecutionProceedings_Executed', pa.int64()),
                ('Pledger_Active', pa.int64()),
                ('Pledger_Ceased', pa.int64()),
                ('Pledgee_Active', pa.int64()),
                ('Pledgee_Ceased', pa.int64())
            ]),
        'BankruptcyMessage': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Date', pa.string()),
                ('DecisionDate', pa.string()),
                ('IdType', pa.string()),
                ('Type', pa.string()),
                ('CaseId', pa.string()),
                ('CaseNumber', pa.string())
            ]),
        'BankruptcyArbitrationCases': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Number', pa.string()),
                ('StatusId', pa.string()),
                ('StatusName', pa.string()),
                ('RegistrationDate', pa.string()),
                ('AcceptanceDate', pa.string()),
                ('SupervisionDate', pa.string()),
                ('ExternalManagementDate', pa.string()),
                ('BankruptcyProceedingsDate', pa.string()),
                ('CompleteDate', pa.string())
            ]),
        'OKVED2List': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Code', pa.string()),
                ('Name', pa.string()),
                ('IsMain', pa.int64()),
                ('IsMainEGRUL', pa.int64()),
                ('IsMainRosstat', pa.int64())
            ]),

        'CharterCapitalHistory': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ActualDate', pa.string()),
                ('CharterCapital', pa.float32())
            ]),
        'ChangesInNameAndLegalForm': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Name', pa.string()),
                ('OGRN', pa.string()),
                ('INN', pa.string()),
                ('OKOP_Code', pa.string()),
                ('OKOP_CodeNew', pa.string()),
                ('OKOP_Name', pa.string()),
                ('ChangeDate', pa.string())
            ]),
        'LeaderList': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ActualDate', pa.string()),
                ('FIO', pa.string()),
                ('Position', pa.string()),
                ('INN', pa.string()),
                ('LegalCapacityEndDate', pa.string()),
                ('ManagementCompany', pa.string()),
                ('ManagementCompanyINN', pa.string()),
                ('RegisterNumber', pa.string()),
                ('Article', pa.string()),
                ('StartDate', pa.string()),
                ('EndDate', pa.string()),
                ('Period', pa.string()),
                ('DisqualifiedInCompany', pa.string())
            ]),
        'Addresses': pa.schema(
            [
                ('SparkID', pa.string()),
                ('TypeAddress', pa.string()),
                ('PostCode', pa.string()),
                ('Address', pa.string()),
                ('Region', pa.string()),
                ('Rayon', pa.string()),
                ('City', pa.string()),
                ('StreetName', pa.string()),
                ('BuildingType', pa.string()),
                ('BuildingNumber', pa.string()),
                ('HousingType', pa.string()),
                ('Housing', pa.string()),
                ('RoomType', pa.string()),
                ('Room', pa.string()),
                ('Longitude', pa.string()),
                ('Latitude', pa.string()),
                ('FiasGUID', pa.string()),
                ('IsHouseFiasGUID', pa.int64()),
                ('FiasCode', pa.string()),
                ('FiasRegion', pa.string()),
                ('FiasArea', pa.string()),
                ('FiasCity', pa.string()),
                ('FiasPlace', pa.string()),
                ('FiasPlan', pa.string()),
                ('FiasStreet', pa.string()),
                ('ActualDate', pa.string()),
                ('BlockType', pa.string()),
                ('Block', pa.string()),
                ('BusinessCenterName', pa.string())
            ]),
        'PhoneList': pa.schema(
            [
                ('SparkID', pa.string()),
                ('TypePhone', pa.string()),
                ('Code', pa.string()),
                ('Number', pa.string()),
                ('Status', pa.string()),
                ('VerificationDate', pa.string()),
                ('IsOpenData', pa.int64()),
                ('Value', pa.string())
            ]),
        'IncludeInList': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('IsNegative', pa.int8()),
                ('ListName', pa.string())
            ]),
        'IncludeInList_AddInfo': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Name', pa.string()),
                ('TextField', pa.string())
            ]),
        'AddInfo': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Id', pa.string()),
                ('Name', pa.string()),
                ('TextField', pa.string())
            ]),
        'ConsolidatedIndicator': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Value', pa.string()),
                ('Description', pa.string()),
                ('Name', pa.string()),
                ('Indicator', pa.string())
            ]),
        'RegistrationInFunds': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('RegistrationDate', pa.string()),
                ('DeregistrationDate', pa.string()),
                ('RegisterNumber', pa.string()),
                ('RegAuthority', pa.string())
            ]),
        'SubmittedStatements': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Form', pa.string()),
                ('ReferenceNumber', pa.string()),
                ('SubmissionDate', pa.string()),
                ('AvailabilityDate', pa.string()),
                ('GRN', pa.string()),
                ('DecisionType', pa.string())
            ]),
        'RegistrationCertificates': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Series', pa.string()),
                ('Number', pa.string()),
                ('IssueDate', pa.string()),
                ('GRN', pa.string())
            ]),
        'Finance': pa.schema(
            [
                ('SparkID', pa.string()),
                ('BalanceType', pa.int64()),
                ('PeriodName', pa.string()),
                ('DateBegin', pa.string()),
                ('DateEnd', pa.string()),
                ('Form', pa.string()),
                ('Section', pa.string()),
                ('Name', pa.string()),
                ('Code', pa.string()),
                ('Value', pa.float64()),
                ('IdFinPok', pa.string())
            ]),
        'BoardOfDirectors_ExecutiveBody': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('ActualDate', pa.string()),
                ('Name', pa.string()),
                ('INN', pa.string()),
                ('BirthdayYear', pa.string()),
                ('Position_Code', pa.string()),
                ('Position_Name', pa.string()),
                ('SharePart', pa.string())
            ]),
        'PersonsWithoutWarrant': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ActualDate', pa.string()),
                ('FIO', pa.string()),
                ('Position', pa.string()),
                ('INN', pa.string()),
                ('LegalCapacityEndDate', pa.string())
            ]),
        'StateContracts': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('Year', pa.string()),
                ('AdmittedNumber', pa.int64()),
                ('NotAdmittedNumber', pa.int64()),
                ('WinnerNumber', pa.int64()),
                ('SignedNumber', pa.int64()),
                ('Sum', pa.float64())
            ]),
        'ArbitrationCases': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Total', pa.int64()),
                ('Considered', pa.int64()),
                ('Appealed', pa.int64()),
                ('DecisionsAndRulings', pa.int64()),
                ('Completed', pa.int64()),
                ('Year', pa.string()),
                ('Plaintiff_CasesNumber', pa.int64()),
                ('Plaintiff_Sum', pa.float32()),
                ('Defendant_CasesNumber', pa.int64()),
                ('Defendant_Sum', pa.float32()),
                ('ThirdOrOtherPerson_CasesNumber', pa.int64())
            ]),
        'StaffNumberFTS': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ActualDate', pa.string()),
                ('Number', pa.int64()),
            ]),
        'AccessibleFinData': pa.schema(
            [
                ('SparkID', pa.string()),
                ('IDPeriod', pa.string()),
                ('Name', pa.string()),
                ('EndDate', pa.string())
            ]),
        'FrozenAccounts': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Number', pa.string()),
                ('Date', pa.string()),
                ('Id', pa.string()),
                ('TaxAuthority_Name', pa.string()),
                ('Code', pa.string()),
                ('Name', pa.string()),
                ('BIK', pa.string()),
                ('Bank_SparkID', pa.string()),
                ('Bank_Name', pa.string()),
            ]),
        'FinanceAndTaxesFTS': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('Income', pa.float32()),
                ('Expenses', pa.float32()),
                ('Period_EndDate', pa.string()),
                ('Total_Sum', pa.float32()),
                ('Id', pa.string()),
                ('Name', pa.string()),
                ('Taxes_Sum', pa.float32()),
                ('TaxArrears_DebtSum', pa.float32()),
                ('TaxArrears_FinesSum', pa.float32()),
                ('TaxArrears_PenaltiesSum', pa.float32())
            ]),
        'SpecialTaxRegimes': pa.schema(
            [
                ('SparkID', pa.string()),
                ('ActualDate', pa.string()),
                ('Code', pa.string()),
                ('Name', pa.string())
            ]),
        'Coowners': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('ShareHolderCount', pa.string()),
                ('ActualDate', pa.string()),
                ('Fullname', pa.string()),
                ('Name', pa.string()),
                ('Address', pa.string()),
                ('Manager', pa.string()),
                ('ManagerInn', pa.string()),
                ('OKOPFName', pa.string()),
                ('Affiliated_SparkID', pa.string()),
                ('INN', pa.string()),
                ('OGRN', pa.string()),
                ('OKPO', pa.string()),
                ('OKATO', pa.string()),
                ('Country_Code', pa.string()),
                ('Country_Name', pa.string()),
                ('TypeHolder', pa.string()),
                ('IsCompany', pa.string()),
                ('SharePart', pa.string())
            ]),
        'Branches': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Type', pa.string()),
                ('Fullname', pa.string()),
                ('Name', pa.string()),
                ('Address', pa.string()),
                ('Manager', pa.string()),
                ('ManagerInn', pa.string()),
                ('OKOPFName', pa.string()),
                ('Affiliated_SparkID', pa.string()),
                ('INN', pa.string()),
                ('OGRN', pa.string()),
                ('OKPO', pa.string()),
                ('OKATO', pa.string()),
                ('OpenDate', pa.string()),
                ('TermDate', pa.string()),
            ]),
        'BranchesEgrul': pa.schema(
            [
                ('SparkID', pa.string()),
                ('Address', pa.string())
            ])
    },
    'GetChangedCompanies': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('IsNew', pa.int8()),
            ('Date', pa.string()),
            ('Change_status', pa.string())
        ])
    },
    'GetChangedEntrepreneurs': {
        'Main': pa.schema(
        [
            ('SparkID', pa.string()),
            ('INN', pa.string()),
            ('OGRNIP', pa.string()),
            ('IsNew', pa.int8()),
            ('Date', pa.string()),
            ('Change_status', pa.string())
        ])
    },

    # ======================= 4 ===========================
    'GetCompanyBeneficiariesAndAffiliates': {
        'Main' : pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'BeneficiariesAndAffiliates': pa.schema([
            ('SparkID', pa.string()),
            ('Face', pa.string()),
            ('Type', pa.string()),
            ('IsFinal', pa.string()),
            ('Name', pa.string()),
            ('SparkID_Face', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('Country_Code', pa.string()),
            ('Country_Name', pa.string()),
            ('Type_Id', pa.string()),
            ('Type_Name', pa.string())
        ])
    },
    'GetOwnershipHierarchy': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('EDRPU', pa.string()),
            ('RNN', pa.string()),
            ('BIN', pa.string()),
            ('OKATO', pa.string()),
            ('EGRPOIncluded', pa.int8()),
            ('EGRULLikvidation', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'Coowners': pa.schema([
            ('SparkID', pa.string()),
            ('Id', pa.string()),
            ('ParentId', pa.string()),
            ('Level', pa.string()),
            ('Name', pa.string()),
            ('SparkID_Coowner', pa.string()),
            ('Address', pa.string()),
            ('Country_Code', pa.string()),
            ('Country_Name', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKOPF_Code', pa.string()),
            ('OKOPF_Name', pa.string()),
            ('OKOPF_CodeNew', pa.string()),
            ('OKATO', pa.string()),
            ('EDRPU', pa.string()),
            ('RNN', pa.string()),
            ('Manager', pa.string()),
            ('SharePart', pa.float64()),
            ('SharePartRUR', pa.float64()),
            ('IndirectSharePart', pa.float64()),
            ('CoownerType', pa.string()),
            ('ActualDate', pa.string())
        ])
    },
    'GetCompanyStructure': {
        'Main': pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('EGRPOIncluded', pa.int8()),
            ('EGRULLikvidation', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'Coowners': pa.schema([
            ('SparkID', pa.string()),
            ('Type', pa.string()),
            ('ActualDate', pa.string()),
            ('ShareHoldersCount', pa.int64()),
            ('Name', pa.string()),
            ('SparkID_Coowner', pa.string()),
            ('Address', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKOPFName', pa.string()),
            ('Manager', pa.string()),
            ('ManagerInn', pa.string()),
            ('FullName', pa.string()),
            ('OKATO', pa.string()),
            ('Country_Code', pa.string()),
            ('Country_Name', pa.string()),
            ('TypeHolder', pa.string()),
            ('IsCompany', pa.string()),
            ('SharePart', pa.string()),
            ('SharePartRUR', pa.float64()),
            ('LegalCapacityEndDate', pa.string()),
            ('InputDate', pa.string()),
            ('CoownerType', pa.string())
        ]),
        'CoownerEGRUL_Pledge': pa.schema([
            ('SparkID', pa.string()),
            ('Coowner_INN', pa.string()),
            ('ContractNumber', pa.string()),
            ('ContractDate', pa.string()),
            ('RegistrationDate', pa.string()),
            ('GRN', pa.string()),
            ('NotaryFIO', pa.string()),
            ('Term', pa.string()),
            ('Name', pa.string()),
            ('SparkID_Pledgee', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string())
        ]),
        'Branch': pa.schema([
            ('SparkID', pa.string()),
            ('Type', pa.string()),
            ('Name', pa.string()),
            ('SparkID_Branch', pa.string()),
            ('AddressOrComment', pa.string()),
            ('OpenDate', pa.string()),
            ('TermDate', pa.string()),
            ('Manager', pa.string()),
            ('ManagerInn', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKOPFName', pa.string()),
            ('FullName', pa.string()),
            ('OKATO', pa.string()),
            ('KPP', pa.string()),
            ('Address', pa.string())
        ]),
        'AffiliatedCompanies':  pa.schema([
            ('SparkID', pa.string()),
            ('Type', pa.string()),
            ('ActualDate_AffiliatedCompanies', pa.string()),
            ('Name', pa.string()),
            ('SparkID_Coowner', pa.string()),
            ('Address', pa.string()),
            ('SharePart', pa.string()),
            ('SharePartRUR', pa.float64()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('Manager', pa.string()),
            ('ManagerInn', pa.string()),
            ('OKOPFName', pa.string()),
            ('FullName', pa.string()),
            ('OKATO', pa.string()),
            ('ActualDate', pa.string())
        ]),
        'NonprofitOrganizationsRosstat': pa.schema([
            ('SparkID', pa.string()),
            ('Name', pa.string()),
            ('SparkID_NonprofitOrganization', pa.string()),
            ('Address', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('Manager', pa.string()),
            ('ManagerInn', pa.string()),
            ('OKOPFName', pa.string()),
            ('FullName', pa.string()),
            ('OKATO', pa.string())
        ])
    },
    'GetCompanyPredecessorSuccessor': {
        'Main' : pa.schema([
            ('SparkID', pa.string()),
            ('ShortName', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('OKPO', pa.string()),
            ('OKATO', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Code', pa.string()),
            ('Status_Text', pa.string()),
            ('Status_Date', pa.string())
        ]),
        'Reorganizations' : pa.schema([
            ('SparkID', pa.string()),
            ('Type', pa.string()),
            ('Current', pa.int8()),
            ('Face_SparkID', pa.string()),
            ('Name', pa.string()),
            ('Address', pa.string()),
            ('INN', pa.string()),
            ('OGRN', pa.string()),
            ('FullName', pa.string()),
            ('Status_IsActing', pa.int8()),
            ('Status_Text', pa.string()),
            ('Status_Code', pa.string()),
            ('Status_Date', pa.string())
        ])
    }
}
