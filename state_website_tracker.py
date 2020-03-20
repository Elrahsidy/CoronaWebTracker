from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.options import Options
import time
from datetime import date
import os
from os import path
import pdfkit
#Dictionary that includes each state and website
stateDict = {
    "cdc" : "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html#2019coronavirus-summary",
    "Alabama" : "http://www.alabamapublichealth.gov/infectiousdiseases/2019-coronavirus.html",
    "Alaska" : "http://dhss.alaska.gov/dph/Epi/id/Pages/COVID-19/default.aspx",
    "Arizona" : "https://www.azdhs.gov/preparedness/epidemiology-disease-control/infectious-disease-epidemiology/index.php#novel-coronavirus-home",
    "Arkansas" : "https://www.healthy.arkansas.gov/programs-services/topics/novel-coronavirus",
    "California" : "https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/Immunization/ncov2019.aspx",
    "Colorado" : "https://covid19.colorado.gov/data",
    "Connecticut" : "https://portal.ct.gov/Coronavirus",
    "Delaware" : "https://www.dhss.delaware.gov/dhss/dph/epi/2019novelcoronavirus.html",
    "District of Columbia" : "https://coronavirus.dc.gov/page/coronavirus-data",
    "Florida" : "https://floridahealthcovid19.gov/",
    "Georgia" : "https://dph.georgia.gov/covid-19-daily-status-report",
    "Hawaii" : "https://health.hawaii.gov/docd/advisories/novel-coronavirus-2019/",
    "Idaho" : "https://coronavirus.idaho.gov/",
    "Illinois" : "http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus",
    "Indiana" : "https://www.in.gov/coronavirus/index.htm",
    "Iowa" : "https://idph.iowa.gov/Emerging-Health-Issues/Novel-Coronavirus",
    "Kansas" : "https://govstatus.egov.com/coronavirus",
    "Kentucky" : "https://govstatus.egov.com/kycovid19",
    "Louisiana" : "http://ldh.la.gov/Coronavirus/",
    "Maine" : "https://www.maine.screen_shotgov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml",
    "Maryland" : "https://coronavirus.maryland.gov/",
    "Massachusetts" : "https://www.mass.gov/info-details/covid-19-cases-quarantine-and-monitoring",
    "Michingan" : "https://www.michigan.gov/coronavirus",
    "Minnesota" : "https://www.health.state.mn.us/diseases/coronavirus/situation.html",
    "Mississippi" : "https://msdh.ms.gov/msdhsite/_static/14,0,420.html",
    "Missouri" : "https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/",
    "Montana" : "https://dphhs.mt.gov/publichealth/cdepi/diseases/coronavirusmt",
    "Nebraska" : "http://dhhs.ne.gov/Pages/Coronavirus.aspx#SectionLink3",
    "Nevada" : "http://dpbh.nv.gov/Programs/OPHIE/dta/Hot_Topics/Coronavirus/",
    "New Hampshire" : "https://www.nh.gov/covid19/",
    "New Jersey" : "https://www.nj.gov/health/cd/topics/covid2019_dashboard.shtml",
    "New Mexico" : "https://cv.nmhealth.org/",
    "New York" : "https://www1.nyc.gov/site/doh/health/health-topics/coronavirus.page",
    "North Carolina" : "https://www.ncdhhs.gov/covid-19-case-count-nc",
    "North Dakota" : "https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases",
    "Ohio" : "https://coronavirus.ohio.gov/wps/portal/gov/covid-19/",
    "Oklahoma" : "https://coronavirus.health.ok.gov/",
    "Oregon" : "https://govstatus.egov.com/OR-OHA-COVID-19",
    "Pennsylvania" : "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx",
    "Rhode Island" : "https://health.ri.gov/data/covid-19/",
    "South Carolina" : "https://www.scdhec.gov/monitoring-testing-covid-19",
    "South Dakota" : "https://doh.sd.gov/news/coronavirus.aspx",
    "Tennessee" : "https://www.tn.gov/health/cedep/ncov.html",
    "Texas" : "https://www.dshs.texas.gov/news/updates.shtm#coronavirus",
    "Utah" : "https://coronavirus.utah.gov/latest/",
    "Vermont" : "https://www.healthvermont.gov/response/infectious-disease/2019-novel-coronavirus",
    "Virginia" : "http://www.vdh.virginia.gov/coronavirus/",
    "Washington" : "https://www.doh.wa.gov/Emergencies/Coronavirus",
    "West Virginia" : "https://dhhr.wv.gov/COVID-19/Pages/default.aspx",
    "Wisconsin" : "https://www.dhs.wisconsin.gov/outbreaks/index.htm",
    "Wyoming" : "https://health.wyo.gov/publichealth/infectious-disease-epidemiology-unit/disease/novel-coronavirus/",
    "Puerto Rico" : "http://www.salud.gov.pr/Pages/coronavirus.aspx",
    "Virgin Islands" : "https://doh.vi.gov/covid19usvi",
    "Guam" : "http://dphss.guam.gov/2019-novel-coronavirus-2019-n-cov/"

}

#Handles creating a directory for each date
date = str(date.today())
directory = os.getcwd()+"/"+date
if path.exists(directory)==False:
    try:
        os.mkdir(directory)
    except OSError:
        print ("Creation of the directory %s failed" % directory )
    else:
        print ("Successfully created the directory %s " % directory)

#The following code is based on the code from an answer on StackOverFlow. link below
#https://stackoverflow.com/questions/51653344/taking-screenshot-of-whole-page-with-python-selenium-and-firefox-or-chrome-headl

for x, y in stateDict.items():
    url = str(y)
    state = str(x)
    driver = webdriver.Chrome()
    #run first time to get scrollHeight
    driver.get(url)
    #pause 3 second to let page load
    time.sleep(3)
    #get scroll Height
    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
    #close browser
    driver.close()
    #Open another headless browser with height extracted above
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size=1920,{height}")
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    #pause 3 second to let page loads
    time.sleep(6)
    #save screenshot
    driver.save_screenshot(directory+'/'+state+'.png')
    print(state + ": Website Image has been downloaded")

    #Downloading the page as pdf
    try:
        print("Downloading " +state+ " website as a pdf file")
        pdfkit.from_url(url, directory+'/'+state+'.pdf')
    except:
        print ("An error occured while downloading pdf file. May or may not download file")
    driver.close()
