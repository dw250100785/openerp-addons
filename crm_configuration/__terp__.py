{
    "name" : "Customer Relationship Management",
    "version" : "1.0",
    "author" : "Tiny",
    "website" : "http://tinyerp.com/module_crm.html",
    "category" : "Generic Modules/CRM & SRM",
    "description": """ The Tiny ERP case and request tracker enables a group of
                   people to intelligently and efficiently manage tasks, issues,
                   and requests. It manages key tasks such as communication, 
                   identification, prioritization, assignment, resolution and notification.""",
    "depends" : ["base","crm"],
    "init_xml" : [],
    "demo_xml" : ["crm_bugs_demo.xml","crm_jobs_demo.xml","crm_lead_demo.xml","crm_meeting_demo.xml"],
    "update_xml" : ["crm_bugs_view.xml","crm_jobs_view.xml","crm_lead_view.xml","crm_meeting_view.xml"],
    "active": False,
    "installable": True
}