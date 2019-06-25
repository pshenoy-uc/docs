# PACER Collective
Members in collective are able to access PACER cases extracted everyday with APIs to..
* List of all the PACER courthouses
* Generate the CSV file containing cases with latest updates for the requested date
* Use the Case ID received in the CSV file to retrieve the source file from the court


## UniCourt's PACER Extractor Details       
   ### 1. Job schedule to fetch new cases
   * #### Daily Extraction Jobs which pulls cases the first time:
        * Runs at 5:00 AM UTC on Tue, Wed, Thu, Fri all UTC time.
        * Pulls filings for last 4 days. This is done because some cases are updated in PACER a few days after the date of filing.
            > Ex: January 15 2019, 5:00am UTC run pulls cases filed from 2019-01-11 to 2019-01-14 
        * Gets the docket information for only cases that were not pulled before
   * #### Weekly Extraction Jobs which pulls cases the first time:
        * Runs at 5:00 AM UTC on Sat UTC time.
        * Pulls for last 2 weeks. This is done because some cases are updated in PACER sometimes upto 2 weeks after the date of filing.
            > Ex: December 29 2018, 5am UTC run pulls cases filed from 2018-12-14 to 2018-12-28
        * Gets the docket information for only cases that were not pulled before. 

   ### 2. Job schedule to update existing cases
   * #### Refresh job for existing cases, 60 days from the date of filings
        * Parties and Attorneys: All are fetched
        * Docket Entries: All docket entries as at the time of extraction from the last docket entry date for that case
 
   ### 3. What details are extracted?
   * Parties and Attorneys: All are fetched
   * Docket Entries: All docket entries as at the time of extraction



## API's

### GET CASES BY LAST UPDATED DATE
   * Get all cases updated on a specific date in a CSV file
   * Last updated date (date in UTC) to be given as the parameter
   * Returns a downloadable link of a CSV as response
   * The link is valid for 60 mins.


### GET CASE SOURCE FILE PATH
   * Get the source file for a the case
   * UniCourt case ID to be given as the parameter
   * Response will be a signed URL containing downloadable link to the source file
   * This link is valid for 60 mins.

### Get the full list of APIs here

## Getting PACER cases and Case Source Files
* Hit the get_cases_by_last_updated_date api in order to get the CSV containing the UniCourt case ID
* Using the case ID retrieved from the above step, make request to the get_case_source_file_path to get the case source file



## Recommended integration methodology

### For getting all the cases with the latest updates, the recommended extraction approach is for a two day extraction setup as follows
* #### Same day run
    * For this setup the last updated date will be the current date
    * The preferred extraction timing for this setup is after 10:00 AM UTC
* #### Negate Run
    * The run will have the last updated date as the previous days date
    * The preferred timing for this extraction 00:15AM UTC, the next day

### The above setup is preferred as
* #### For the same day extraction
  Our daily run which updated the PACER cases hits completion at 9:30AM UTC
* ##### For the negate extraction
  Once the cases are updated by the daily run, there are chances that more cases will be updated by our clients, in this case the negate extractor setup will ensure that even these updated cases are picked.
