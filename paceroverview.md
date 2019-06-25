## UniCourt PACER API's overview

###### UniCourt's partners in the PACER Collective are able to access the cases extracted everyday with the PACER
API's. These API's provide the following data:
* List of all the PACER courthouses
* Retrieve UniCourt case id for a PACER case, known the PACER case ID and the courthouse
* Generating the CSV file for clients which containing the cases with the latest updates for the requested date
* Using the UniCourt case id in the above steps to get the html file for that particular case

## Our API's
##### GET PACER COURTHOUSES
   * ###### To get the list of PACER courthouses
   * ###### Does not have any request parameters

##### GET CASE ID FOR PACER CASES
   * ###### To get the UniCourt case ID for a PACER case
   * ###### The PACER case ID and the courthouse should be provided as parameters

##### GET CASE SOURCE FILE PATH
   * ###### To get the html for a specific case
   * ###### UniCourt case ID to be given as the parameter
   * ###### Response will be a signed URL containing downloadable link to the HTML
   * ###### This link is only valid for the first 60 mins.

##### GET CASES BY LAST UPDATED DATE
   * ###### To get the cases updated on a specific date
   * ###### Last updated date (date) to be given as the parameter
   * ###### Sends a downloadable link to a CSV as response
   * ###### This link is valid for only the first 60 mins.

## Getting PACER cases and HTML
* ##### Hit the get_cases_by_last_updated_date api in order to get the CSV containing the UniCourt case ID
* ##### using the case ID retrieved from the above step, make request to the get_case_source_file_path to get the case HTML

## UniCourt Extractors
* ##### An extractor (fetches 4 days of cases) that starts at 5:00 AM UTC and hits completion at 8:30 AM UTC, but can go up to 9:30 AM UTC depending on the number of cases
 * ##### Another negate 60 extractor which runs at 7:00AM UTC and fetches cases 60 days prior to the current date. 

## Recommended API Integration method

##### For getting all the cases with the latest updates, the recommended extraction approach is for a two day extraction setup as follows
* ##### Same day run
    * For this setup the last updated date will be the current date
    * The preferred extraction timing for this setup is after 10:00 AM UTC
* ##### Negate Run
    * The run will have the last updated date as the previous days date
    * The preferred timing for this extraction 00:15AM UTC, the next day

##### The above setup is preferred as
* ##### For the same day extraction
     ###### Our daily run which updated the PACER cases hits completion at 9:30AM UTC
* ##### For the negate extraction
    ###### Once the cases are updated by the daily run, there are chances that more cases will be updated by our clients, in this case the negate extractor setup will ensure that even these updated cases are picked.
