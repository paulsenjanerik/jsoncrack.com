import pprint
from dataclasses import dataclass
from tabulate import tabulate
import json
import sys

print("Dette programmet heter:", sys.argv[0])

## TODO Riktig server for riktig skript


@dataclass
class Node:
    "En node. Template for resten av klassene"
    navn: str
    beskrivelse: str
    kommentar: str
    aktiv: str
    versjon: str


@dataclass
class VM(Node):
    "En virtuell maskin i VMWare"
    os: str
    ip: str
    cpu: str
    ram: str
    hypervisor: str
    applikasjoner: []
    scripts: []
    lisenser: []

    def lag_node(self):

        apps = []
        for i in self.applikasjoner:
            apps.append(i)

        scripts = []
        for i in self.scripts:
            scripts.append(i)

        lisenser = []
        for i in self.lisenser:
            lisenser.append(i)

        data = {
            "Navn": self.navn,
            "Beskrivelse": self.beskrivelse,
            "Kommentar": self.kommentar,
            "Aktiv": self.aktiv,
            "Versjon": self.versjon,
            "OS": self.os,
            "CPU": self.cpu,
            "RAM": self.ram,
            "Hypervisor": self.hypervisor,
            "applikasjoner": apps,
            "scripts": scripts,
            "lisenser": lisenser,
        }
        data = str(data).replace("'", '"')

        return data


@dataclass
class Applikasjon(Node):
    "En applikasjon som er installert på en VM"
    web_apps: []

    def __repr__(self):
        apps = []
        for i in self.web_apps:
            apps.append(i)

        data = {
            "Navn": self.navn,
            "Beskrivelse": self.beskrivelse,
            "Kommentar": self.kommentar,
            "Aktiv": self.aktiv,
            "Versjon": self.versjon,
            "Apps": apps,
        }
        data = str(data).replace("'", '"')

        return data


@dataclass
class Web_app(Node):
    "En webapplikasjon i SharePoint eller i IIS"
    eier: str
    gruppe: str
    dokumentasjon: str
    avhengigheter: []
    url: str

    def __repr__(self):
        data = {
            "Navn": self.navn,
            "Beskrivelse": self.beskrivelse,
            "Kommentar": self.kommentar,
            "Aktiv": self.aktiv,
            "Versjon": self.versjon,
            "Eier": self.eier,
            "Gruppe": self.gruppe,
            "Dokumentasjon": self.dokumentasjon,
            "Avhengigheter": self.avhengigheter,
            "Url": self.url,
        }
        data = str(data).replace("'", '"')

        return data


@dataclass
class Lisens(Node):
    "En lisens"
    kost: float

    def __repr__(self):
        data = {
            "Navn": self.navn,
            "Beskrivelse": self.beskrivelse,
            "Kommentar": self.kommentar,
            "Aktiv": self.aktiv,
            "Versjon": self.versjon,
            "Kost": self.kost,
        }
        data = str(data).replace("'", '"')

        return data


### Definisjoner VM ###
nokrssrv610sp = VM(
    navn="nokrssrv610sp.anyaccess.net",
    beskrivelse="Serverhost for SP2016",
    kommentar="EOL 2023",
    aktiv="true",
    versjon="2012 R2",
    os="Microsoft Server",
    ip="10.47.1.239",
    cpu="2x Intel Xeon Silver 4214 CPU @ 2.20GHz",
    ram="32 GiB Synchronous DRAM",
    hypervisor="VMware Virtual Platform",
    applikasjoner=[],
    scripts=["10 siste Synergi kommplatt", "Rundelister_kvittering", "SPWarmup"],
    lisenser=[],
)
nokrssrv611sp = VM(
    navn="nokrssrv611sp.anyaccess.net",
    beskrivelse="Serverhost for Intrafnis og statiske websider",
    kommentar="EOL 2023",
    aktiv="true",
    versjon="2012 R2",
    os="Microsoft Server",
    ip="10.47.1.170",
    cpu="Intel Xeon CPU E5-2650 v4 @ 2.20GHz",
    ram="64 GiB DRAM",
    hypervisor="VMware Virtual Platform",
    applikasjoner=[],
    scripts=[
        "doksys-pdf",
        "mikon_flyttefiler",
        "oppdatere 10 siste synergi",
        "oppdatere telefonliste",
        "autonyhet",
        "sikkerhetsbudskap",
        "Robotkjetil"
    ],
    lisenser=[],
)
nokrssrv612sp = VM(
    navn="nokrssrv612sp.anyaccess.net",
    beskrivelse="Serverhost for Doksys mm.",
    kommentar="EOL 2023",
    aktiv="true",
    versjon="2012 R2",
    os="Microsoft Server",
    ip="10.47.1.103",
    cpu="Intel Xeon CPU E5-2650 v4 @ 2.20GHz",
    ram="64 GiB DRAM",
    hypervisor="VMware Virtual Platform",
    applikasjoner=[],
    scripts=["Doksys-backup", "Doksys-pdf"],
    lisenser=[],
)
nonkrssrv401 = VM(
    navn="nonkrssrv401.anyaccess.net",
    beskrivelse="Databaser primært ment for SharePoint",
    kommentar="EOL 2023",
    aktiv="true",
    versjon="2012 R2",
    os="Microsoft Server",
    ip="10.47.1.50",
    cpu="2x Intel Xeon CPU E5-2650 v4 @ 2.20GHz",
    ram="32 GiB Synchronous DRAM",
    hypervisor="VMware Virtual Platform",
    applikasjoner=[],
    scripts=[],
    lisenser=[],
)
nokrssrv4sp = VM(
    navn="nokrssrv4sp.anyaccess.net",
    beskrivelse="Databaser primært ment for SharePoint",
    kommentar="EOL 2023",
    aktiv="true",
    versjon="2012 R2",
    os="Microsoft Server",
    ip="10.47.4.102",
    cpu="2x Intel Xeon CPU E5-2650 v4 @ 2.20GHz",
    ram="32 GiB DRAM",
    hypervisor="VMware Virtual Platform",
    applikasjoner=[],
    scripts=[],
    lisenser=[],
)

### Definisjoner Applikasjoner ###
sp610 = Applikasjon(
    navn="SharePoint Server",
    beskrivelse="Samhandlingsplattform fra Microsoft",
    kommentar="Bør konsolideres og oppgraderes",
    aktiv="true",
    versjon="2016",
    web_apps=[],
)
sp611 = Applikasjon(
    navn="SharePoint Server",
    beskrivelse="Samhandlingsplattform fra Microsoft",
    kommentar="Bør konsolideres og oppgraderes",
    aktiv="true",
    versjon="2013",
    web_apps=[],
)
sp612 = Applikasjon(
    navn="SharePoint Server",
    beskrivelse="Samhandlingsplattform fra Microsoft",
    kommentar="Bør konsolideres og oppgraderes",
    aktiv="true",
    versjon="2013",
    web_apps=[],
)
db401 = Applikasjon(
    navn="SQL Server 2014 Standard Edition (64-bit)",
    beskrivelse="Database",
    kommentar="Relasjoner: nokrssrv611sp",
    aktiv="true",
    versjon="2014",
    web_apps=[
        "New_NBS",
        "Word",
        "2022_WSS_UsageApplication",
        "611_NintexForms",
        "testmiljo_okt_2021_doksys",
        "testmiljo_doksys",
        "SSA2021_LinksStoreDB_7baf6499e1234675a7c21dd0aa9b0082",
        "SSA2021_AnalyticsReportingStoreDB_44ddb9e416e249bca10b024f6a248036",
        "SSA2021_CrawlStoreDB_e8ae9c61bd9543b1810e69c9f3075614",
        "SSA_2020__CrawlStoreDB_f9733b1c7e5c4ab2b49f360733557ec0",
        "SSA2021_DB_acf6be3f638d4a6a828de29dcda19b1e",
        "SSA_2020__LinksStoreDB_a4264115fa87470d94de73f74f4a7e53",
        "SSA_2020__AnalyticsReportingStoreDB_434888de4f0743d98b1ec78b086c4105",
        "SSA_2020__DB_1b84de24a410492a9c9b288117b0f848",
        "Bdc_Service_DB_0da1346b1ac8464f9cf9f1886995059e",
        "AppMng_Service_DB_72a175b64ca6484984449f507e4a2fa9",
        "TranslationService_e20f7209d4ea43e08f1327d773d77898",
        "PerformancePoint",
        "2020_UPA_4_Social",
        "WSS_Content_799a12bd62d0424dacb1554781df9305",
        "2020_UPA_4_Sync",
        "2020_UPA_4_Profile",
        "612SP_UPA_3_Social",
        "612SP_UPA_3_Sync",
        "612SP_UPA_3_Profile",
        "Word_Automation_DB",
        "612_MySite",
        "Lab",
        "612SP_UPA_1_Social",
        "612SP_UPA_1_Profile",
        "612SP_UPA_1_Sync",
        "User",
        "User",
        "User",
        "NBS_newContent",
        "612_Search",
        "612_NintexForms",
        "WSS_Content_34711306913e4324b1be394d08a72634",
        "611_skift",
        "612_tempDB_slett",
        "NBS_skift",
        "612_NBS_MetaData",
        "612_NBS_migratefrom610",
        "612_NBS",
        "612_NintexWFDB",
        "612_NW2013DB_new",
        "611SP_NW2013DB",
        "612_NW2013DB",
        "612_Skift_ContentDB",
        "612_Kommunikasjonsplattform",
        "NBS_Skift_Rormerk",
        "NBS_Skift_InitialTemp",
        "Search_Service_Application_1_AnalyticsReportingStoreDB_07e2fe152e7346a6912ace04a551de32",
        "Search_Service_Application_1_LinksStoreDB_14aa67c0fcbc41d4b73a8e5370eebeaf",
        "Search_Service_Application_1_DB_c36a4d66ae064f6790d4d6b6c93e5e51",
        "Search_Service_Application_1_CrawlStoreDB_552829c4b2a94c329a74f0a44421b600",
        "prod2_SecureStore",
        "prod2_UsageAndHealth",
        "prod2_MetaData",
        "prod2_StateService",
        "prod2_defaultSite",
        "prod2_contentDB",
        "prod2_Content_CentralAdmin",
        "prod2_Config",
        "Search15_LinksStore",
        "Search15_AnalyticsReportingStore",
        "Search15_CrawlStore",
        "NBS_Social",
        "Search15",
        "NBS_Sync",
        "NBS_Profile",
        "Intra_MySite",
        "UPA2_Profile",
        "UPA2_Social",
        "UPA2_Sync",
        "NBS_Social",
        "NBS_Sync",
        "NBS_Profile",
        "NBS-Social",
        "NBS-Sync",
        "NBS-Profile",
        "Sync",
        "Social",
        "Social",
        "Test",
        "WSS_Content_35f51da7b41447c7903a9859ebd42069",
        "test2",
        "testmiljo_okt_2021",
        "Sharepoint_Dokstyring",
        "Xstrata_WSS_Conten_old",
        "Nikkelverk_Sharepoint",
        "Search_Service_Application_1_LinksStoreDB_e9a508149d374916894639cf05b0fc16",
        "Search_Service_Application_1_CrawlStoreDB_d6a20c18396047fe85e7b46e6ba809f3",
        "Search_Service_Application_1_AnalyticsReportingStoreDB_b1ac09baacb3473bb92d9f86b880681f",
        "Intra_MetaData",
        "Intra_UsageAndHealth",
        "Intra_SecureStore",
        "Search_Service_Application_1_DB_53a2d7352f84477e9f684b412e9a1d8d",
        "Intra_StateService",
        "Intra_intrafnis",
        "WAS",
        "Intra_Content_CentralAdmin",
        "Search_Service_Application_2_LinksStoreDB_a05e488a780449fab788e4f007924a7e",
        "Intra_Config",
        "NW2013DB",
        "Search_Service_Application_2_DB_5bff88cc9cdc4ab8951b5ac2c1188166",
        "Search_Service_Application_2_AnalyticsReportingStoreDB_7a4b1f5b39a741acb74ffe458432186e",
        "Search_Service_Application_2_CrawlStoreDB_5cf9d0b0969e43b79f30a3089332f942",
        "WSS_Content",
        "NintexForms",
        "Skift_Content",
        "NBS_dokstyring",
        "Profile",
        "Sync",
        "Profile",
        "SP2013DEV-SubscriptionSettingsDB",
        "SP_2013_App_Management_Service_App",
        "SP_2013_Subscriptions_Service_App",
        "WFInstanceManagementDB",
        "WFResourceManagementDB",
        "tempdb",
        "model",
        "NBS_SecureStore",
        "WFManagementDB",
        "SBMessageContainer01",
        "NBS_Search_LinksStore",
        "NBS_Search_AnalyticsReportingStore",
        "SbManagementDB",
        "NBS_Search",
        "NBS_UsageAndHealth",
        "SbGatewayDatabase",
        "NBS_Search_CrawlStore",
        "NBS_Config",
        "NBS_dokumentstyring",
        "NBS_Content_CentralAdmin",
        "NBS_MetaData",
        "msdb",
        "NBS_StateService",
        "mssqlsystemresource",
        "master",
    ],
)
db4sp = Applikasjon(
    navn="SQL Server 2017 Standard Edition (64-bit)",
    beskrivelse="Database",
    kommentar="Relasjoner: nokrssrv610sp og nokrssrv611sp",
    aktiv="true",
    versjon="2017",
    web_apps=[
        "GDPR_content",
        "_NBS",
        "dev",
        "AppServiceDB",
        "SettingsServiceDB",
        "testmiljo",
        "Kommunikasjonsplattform_temp",
        "Bdc_Service_DB_db320436a5f64ae4891bb4ed2ccba2b9",
        "610_UPA_Social",
        "Sync_7387b1cb-d44f-4824-8008-e1fd59fe966c",
        "Search_Service_Application_LinksStoreDB_fef5b361fcb147d58887c8254549ff06",
        "AppMng_Service_DB_d60b103cab2c457eac15f1aed2965f5a",
        "tempdb",
        "Apps",
        "610_UPA_Profile",
        "Kommunikasjonsplattform",
        "Search_Service_Application_CrawlStoreDB_fe9d6dd8e30040bf98d719bcb6cf3b1e",
        "Search_Service_Application_AnalyticsReportingStoreDB_f960351860694248ab822b43e78467f5",
        "WordAutomationServices_ad99a959e60b4783ac91bf03cce11f5a",
        "Search_Service_Application_DB_331d5f9e645b4678b0bacf50b6298fc5",
        "prod_2016_SecureStore",
        "TranslationService_920050747df84d7aac078f1cabec7bc6",
        "prod_2016_UsageAndHealth",
        "WSS_Content",
        "prod_2016_StateService",
        "PerformancePoint",
        "NintexFormsDB",
        "model",
        "prod_2016_MetaData",
        "NintexWorkflowDB",
        "prod_2016_Content_CentralAdmin",
        "prod_2016_Config",
        "msdb",
        "mssqlsystemresource",
        "master",
    ],
)
nintex = Applikasjon(
    navn="Nintex: Process Management and Workflow Automation",
    beskrivelse="Low-code-verktøy for automatisering av arbeidsflyter",
    kommentar="Relativt høy kostnad, og kan byttes ut dersom innkoding oppgraderes. www.nintex.com",
    aktiv="true",
    versjon="SaSS",
    web_apps=[],
)
iis610 = Applikasjon(
    navn="Internet Information Services",
    beskrivelse="Webserver",
    kommentar="Hosting av skjemaer og statisk data",
    aktiv="true",
    versjon="",
    web_apps=[
        "Telefonliste",
        "Skiftportal",
        "Personalrapporter",
        "Analysetabell",
        "Lommekniv/verktøykasse",
    ],
)
iis611 = Applikasjon(
    navn="Internet Information Services",
    beskrivelse="Webserver",
    kommentar="Hosting av skjemaer og statisk data",
    aktiv="true",
    versjon="",
    web_apps=[
        "Telefonliste",
        "Skiftportal",
        "Personalrapporter",
        "Taxi",
        "Analysetabell",
        "Utslipp",
        "Overtidsmat",
    ],
)
iis612 = Applikasjon(
    navn="Internet Information Services",
    beskrivelse="Webserver",
    kommentar="Hosting av skjemaer og statisk data",
    aktiv="true",
    versjon="",
    web_apps=[],
)

### Definisjoner Web_apps ###

# 610
merking = Web_app(
    navn="Merking",
    beskrivelse="Registrering av rørmerker",
    kommentar="Usikker hvem som har arvet dette og hvorvidt det brukes",
    aktiv="true",
    versjon="",
    eier="hms",
    gruppe="NBS",
    dokumentasjon="false",
    avhengigheter=["PowerShell"],
    url="http://nokrssrv610sp:8254/sites/merking",
)
innkoding = Web_app(
    navn="Innkoding",
    beskrivelse="Innkoding og godkjenning før sap bulk import",
    kommentar="Sparer penger på å oppgradere denne og få bort Nintex",
    aktiv="true",
    versjon="",
    eier="Innkjøp",
    gruppe="NBS",
    dokumentasjon="false",
    avhengigheter=["Nintex"],
    url="http://nokrssrv610sp:8254/sites/innkoding",
)
kommplatt = Web_app(
    navn="Kommunikasjonsplattform for skift",
    beskrivelse="Stopper, meldinger og oppgaver mellom skift",
    kommentar="Bør kunne byttes ut med teams?",
    aktiv="true",
    versjon="",
    eier="Skift",
    gruppe="komm.platt",
    dokumentasjon="false",
    avhengigheter=["JavaScript", "CSS", "SharePoint Designer Workflow"],
    url="http://nokrssrv610sp:38249/sites/skift",
)

# 611
Intrafnis = Web_app(
    navn="Intrafnis",
    beskrivelse="Nyheter og informasjon",
    kommentar="Intranett",
    aktiv="true",
    versjon="",
    eier="Kvalitet",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter=[
        "PowerShell",
        "JavaScript",
        "InfoPath Designer",
        "SharePoint Designer Workflow",
        "Every branding",
    ],
    url="http://nikkelverk",
)
forbedringslogg = Web_app(
    navn="Forbedringslogg",
    beskrivelse="Loggføring av forbedringer",
    kommentar="Lappverk av arbeidsflyter som må kartlegges",
    aktiv="true",
    versjon="",
    eier="NBS",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter=[
        "PowerShell",
        "JavaScript",
        "InfoPath Designer",
        "SharePoint Designer Workflow",
    ],
    url="",
)
sikkerhetsregistreringer = Web_app(
    navn="Sikkerhetsregistreringer",
    beskrivelse="KPI-registreringer for sikkerhetsrunder",
    kommentar="Hokus-pokus-logikk. Må dokumenteres",
    aktiv="true",
    versjon="",
    eier="NBS",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter=["PowerShell", "InfoPath Designer", "SharePoint Designer Workflow"],
    url="http://nikkelverk/drift/NBS/Sikkerhetsregistreringer",
)
femsrunder = Web_app(
    navn="5S-runder",
    beskrivelse="Loggføring og scoring av 5s-runder",
    kommentar="Kompliserte infopath-konstruksjoner",
    aktiv="true",
    versjon="",
    eier="NBS",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter=["InfoPath Designer", "SharePoint Designer Workflow"],
    url="http://nikkelverk/drift/NBS/Lists/5sinput/AllItems.aspx",
)
leverandorreg = Web_app(
    navn="Leverandørregistreringer",
    beskrivelse="Registrering av nye leverandører (kyc)",
    kommentar="KYC-regler",
    aktiv="true",
    versjon="",
    eier="Innkjøp",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter=["InfoPath Designer", "SharePoint Designer Workflow"],
    url="",
)
pameldinger = Web_app(
    navn="påmeldinger",
    beskrivelse="håndering av deltakere til arrangement",
    kommentar="vanilla SharePoint",
    aktiv="true",
    versjon="",
    eier="Kvalitet",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter="",
    url="http://nikkelverk/pameldinger/",
)
gdpr = Web_app(
    navn="gdpr",
    beskrivelse="håndtering av compliance",
    kommentar="vanilla SharePoint",
    aktiv="true",
    versjon="",
    eier="Kvalitet",
    gruppe="Intrafnis",
    dokumentasjon="false",
    avhengigheter="",
    url="http://nikkelverk/gdpr/",
)
labsys = Web_app(
    navn="labsys",
    beskrivelse="håndtering av dokumenter, målinger og regneark for lab",
    kommentar="må være tilgjengelig fra instrumenter (ot)",
    aktiv="true",
    versjon="",
    eier="analyselaboratoriet",
    gruppe="lab",
    dokumentasjon="false",
    avhengigheter=["Python", "PowerShell", "onedrive"],
    url="http://nokrssrv611sp:1870",
)

# 612
doksys = Web_app(
    navn="Doksys",
    beskrivelse="Håndtering av styrende dokumenter",
    kommentar="Dokumentstyringssystemet",
    aktiv="true",
    versjon="",
    eier="Kvalitet",
    gruppe="NBS",
    dokumentasjon="false",
    avhengigheter=[
        "Nintex",
        "PowerShell",
        "JavaScript",
        "CSS",
        "Visio",
        "SharePoint Designer Workflow"
    ],
    url="http://nokrssrv612sp:27075/sites/dokumentstyring/Dokumentstyring/Forms/NK_.aspx",
)
utleggsys = Web_app(
    navn="Utleggssystem",
    beskrivelse="Godkjenning og refusjon av utlegg",
    kommentar="Deaktivert per september 2022",
    aktiv="false",
    versjon="",
    eier="Regnskap",
    gruppe="NBS",
    dokumentasjon="false",
    avhengigheter=["Nintex", "PowerShell"],
    url="http://nokrssrv612sp:27075/sites/dokumentstyring/skjema/",
)
itsys = Web_app(
    navn="IT-sys 2.0",
    beskrivelse="Inventory og løpenummer for maskinpark",
    kommentar="",
    aktiv="true",
    versjon="",
    eier="it",
    gruppe="NBS",
    dokumentasjon="false",
    avhengigheter=["JavaScript", "CSS"],
    url="http://nokrssrv612sp:27075/sites/dokumentstyring/it/",
)
faktura = Web_app(
    navn="Faktura",
    beskrivelse="Genering av faktura med løpenummer",
    kommentar="Gøy at denne fremdeles brukes",
    aktiv="true",
    versjon="",
    eier="Regnskap",
    gruppe="NBS",
    dokumentasjon="false",
    avhengigheter=["SharePoint Designer Workflow"],
    url="http://nokrssrv612sp:27075/sites/dokumentstyring/faktura/",
)

### Lisenser ###
lisens_sp2016 = Lisens(
    navn="Microsoft Office SharePoint Server 2016 Volume license",
    beskrivelse="",
    kommentar="",
    versjon="2016",
    aktiv="true",
    kost=50000,
)
lisens_sp2013 = Lisens(
    navn="Microsoft Office SharePoint Server 2013 Volume license",
    beskrivelse="",
    kommentar="",
    versjon="2013",
    aktiv="true",
    kost=50000,
)
lisens_dc2016 = Lisens(
    navn="Windows Server 2016 Datacenter",
    beskrivelse="",
    kommentar="",
    versjon="2016",
    aktiv="true",
    kost=50000,
)
lisens_dc2012 = Lisens(
    navn="Windows Server 2012 R2 Datacenter",
    beskrivelse="",
    kommentar="",
    versjon="2012",
    aktiv="true",
    kost=50000,
)
lisens_sql2017 = Lisens(
    navn="SQL Server 2017 Standard Edition",
    beskrivelse="",
    kommentar="",
    versjon="2017",
    aktiv="true",
    kost=10000,
)
lisens_sql2014 = Lisens(
    navn="SQL Server 2014 Standard Edition",
    beskrivelse="",
    kommentar="",
    versjon="2014",
    aktiv="true",
    kost=10000,
)
lisens_spdesigner = Lisens(
    navn="Microsoft SharePoint Designer 2013 Volume license",
    beskrivelse="",
    kommentar="",
    versjon="2013",
    aktiv="true",
    kost=0,
)
lisens_nintex = Lisens(
    navn="Nintex: Process Management and Workflow Automation",
    beskrivelse="Low-code-verktøy for automatisering av arbeidsflyter. www.nintex.com",
    kommentar="Relativt høy kostnad og bør byttes ut dersom innkoding oppgraderes",
    versjon="SaSS",
    aktiv="true",
    kost=200000,
)


### Legge lisenser til klasser
nokrssrv610sp.lisenser = [lisens_sp2016, lisens_dc2016, lisens_nintex]
nokrssrv611sp.lisenser = [lisens_sp2013, lisens_dc2012, lisens_spdesigner]
nokrssrv612sp.lisenser = [
    lisens_sp2013,
    lisens_dc2012,
    lisens_spdesigner,
    lisens_nintex,
]
nokrssrv4sp.lisenser = [lisens_sql2017, lisens_dc2012]
nonkrssrv401.lisenser = [lisens_sql2014, lisens_dc2012]
lisenser_totalt = (
    nokrssrv610sp.lisenser
    + nokrssrv611sp.lisenser
    + nokrssrv612sp.lisenser
    + nokrssrv4sp.lisenser
    + nonkrssrv401.lisenser
)

### Relasjoner ###
## Applikasjoner
nokrssrv610sp.applikasjoner = [sp610, iis610, nintex]
nokrssrv611sp.applikasjoner = [sp611, iis611, nintex]
nokrssrv612sp.applikasjoner = [sp612, iis612, nintex]
nokrssrv4sp.applikasjoner = [db4sp]
nonkrssrv401.applikasjoner = [db401]

### Webapplikasjoner
sp610.web_apps = [merking, innkoding, kommplatt]
sp611.web_apps = [
    Intrafnis,
    forbedringslogg,
    sikkerhetsregistreringer,
    femsrunder,
    leverandorreg,
    pameldinger,
    gdpr,
    labsys,
]
sp612.web_apps = [doksys, utleggsys, itsys, faktura]


total = [
    nokrssrv610sp.lag_node(),
    nokrssrv611sp.lag_node(),
    nokrssrv612sp.lag_node(),
    nokrssrv4sp.lag_node(),
    nonkrssrv401.lag_node(),
]


def lag_json():
    def filbehandling():
        with open("template.jan", "r") as file:
            filedata = file.read()
        filedata = filedata.replace("##PASTE##", val)
        with open("data.ts", "w") as file:
            file.write(filedata)

    start = f"👇👇👇 Kopier dette 👇👇👇 \n\n"
    slutt = f"\n\n 👆👆👆 Kopier dette 👆👆👆\n\n"

    try:
        if len(sys.argv) < 2:
            val = str(total).replace("'", "").replace('"true"', "true")
            with open("template.jan", "r") as file:
                filedata = file.read()
            filedata = filedata.replace("##PASTE##", "")
            with open("data.ts", "w") as file:
                file.write(filedata)
        if sys.argv[1] == "total":
            val = (
                str(total)
                .replace("'", "")
                .replace('"true"', "true")
                .replace('"false"', "false")
            )
            filbehandling()
            print(start)
            print(val)
            print(slutt)
        if sys.argv[1] == "610":
            val = (
                str([str(nokrssrv610sp.lag_node())])
                .replace("'", "")
                .replace('"true"', "true")
                .replace('"false"', "false")
            )
            filbehandling()
            print(start)
            print(val)
            print(slutt)
        if sys.argv[1] == "611":
            val = (
                str([str(nokrssrv611sp.lag_node())])
                .replace("'", "")
                .replace('"true"', "true")
                .replace('"false"', "false")
            )
            filbehandling()
            print(start)
            print(val)
            print(slutt)
        if sys.argv[1] == "612":
            val = (
                str([str(nokrssrv612sp.lag_node())])
                .replace("'", "")
                .replace('"true"', "true")
                .replace('"false"', "false")
            )
            filbehandling()
            print(start)
            print(val)
            print(slutt)
        if sys.argv[1] == "4sp":
            val = (
                str([str(nokrssrv4sp.lag_node())])
                .replace("'", "")
                .replace('"true"', "true")
                .replace('"false"', "false")
            )
            filbehandling()
            print(start)
            print(val)
            print(slutt)
        if sys.argv[1] == "401":
            val = (
                str([str(nonkrssrv401.lag_node())])
                .replace("'", "")
                .replace('"true"', "true")
                .replace('"false"', "false")
            )
            filbehandling()
            print(start)
            print(val)
            print(slutt)
        if sys.argv[1] == "kost":
            print(tabulate([lisenser_totalt]))
    except:
        # sys.exit("Noe galt skjedde")
        pass


def lag_tabeller(obj):

    objekter = [nokrssrv610sp, nokrssrv611sp, nokrssrv612sp, nokrssrv4sp, nonkrssrv401]
    for obj in objekter:
        print(f"\n \n ### Lisenskostnader for {obj.navn} ### \n")
        print(
            tabulate(
                obj.lisenser,
                headers=[
                    "Navn",
                    "Beskrivelse",
                    "Kommentar",
                    "Aktiv",
                    "Versjon",
                    "Kost (ca)",
                ],
                tablefmt="pretty",
            )
        )


lag_json()
# lag_tabeller(nokrssrv610sp)

