import os
from google.cloud import translate
from google.cloud import translate_v2 as translate
import json
import time

start_time = time.time()

en_text={
    "welcome-back": "Welcome back",
    "Project": "Project",
    "Analytics": "Analytics",
    "SEARCH": "Search",
    "FROM": "From",
    "TO": "To",
    "SIGN_IN":{
        "LOGIN_WITH_KONA_ID":"Login with KONA ID",
        "SIGN_IN_TO_NEW_COMMERCE_ADMIN_PANEL":"Sign in to New Commerce admin panel",
        "SIGN_IN":"Sign in"
    },
    "SIGN_OUT": {
        "REDIRECTING_IN": "Redirecting in ",
        "BEING_REDIRECTED": "You are now being redirected",
        "GO_TO": "Go to",
        "SIGN_IN": "Sign in"
    },
    "ERROR_404": {
        "BACK_TO_HOME": "Back to Home",
        "REQUESTED_PAGE_NOT_FOUND": "The page you requested could not be found.",
        "OOPS_TEXT": "Ooops... 404"
    },
    "ERROR_500": {
        "SOMETHING_WENT_WRONG": "Something went wrong",
        "SERVER_ERROR": "Server Error 500. Our staff has been notified, thank you for your understanding.",
        "BACK_TO_DASHBOARD": "Back to Dashboard"
    },
    "USER_PROFILE": {
        "SIGN_IN_AS": "Signed In as",
        "SIGN_OUT": "Sign Out"
    },
    "USER_CREATE":{
        "EDIT_PROFILE": "Edit Profile",
        "ADD_A_NEW_USER" : "Add a New User",
        "FIRST_NAME": "First Name",
        "LAST_NAME": "Last Name",
        "EMAIL":"Email",
        "SELECT_ROLE": "Role",
        "PHONE": "Phone",
        "UPDATE" : "Update",
        "CREATE_USER":"Create User",
        "CANCEL":"Cancel",
        "DATE_OF_BIRTH":"Date of Birth",
        "DATE_PICKER_PLACEHOLDER_SELECT":"Select",
        "ERROR_UPLOADING_PROFILE_PICTURE": "Error Uploading Profile Picture",
        "FIRST_NAME_REQUIRED":"First name is required",
        "FIRST_NAME_MINLENGTH":"First name should be at least 2 character",
        "FIRST_NAME_MAXLENGTH": "First name should be at most 40 character",
        "FIRST_NAME_PATTERN": "First name should only contain letters. Spaces are allowed except first position",
        "LAST_NAME_REQUIRED":"Last name is required",
        "LAST_NAME_MINLENGTH":"Last name should be at least 2 character",
        "LAST_NAME_MAXLENGTH": "Last name should be at most 40 character",
        "LAST_NAME_PATTERN": "Last name should only contain letters. Spaces are allowed except first position",
        "EMAIL_REQUIRED": "Email address is required",
        "EMAIL_INVALID": "Invalid Email Address. Hint: abc@xys.com",
        "EMAIL_EXIST": "Email Address Already Exists",
        "ROLE_REQUIRED": "Role is required",
        "PHONE_INVALID": "Invalid Phone Number. Hint: +xxxxxxxxxx or +xxxxxxxxxxx"
    },
    "USER_TABLE":{
        "NAME": "NAME",
        "EMAIL":"EMAIL",
        "USER_ROLE": "USER ROLE",
        "STATUS": "STATUS",
        "LAST_LOGGED_IN":"LAST LOGGED IN",
        "ACTIVE": "Active",
        "INACTIVE": "Inactive",
        "VIEW": "View",
        "EDIT": "Edit"
    },
    "USER_LIST":{
        "ALL_USER":"All Users",
        "ADD_NEW_USER": "Add New User",
        "USER_ROLE": "User Role:",
        "ALL": "All",
        "STATUS": "Status:",
        "ACTIVE": "Active",
        "INACTIVE": "Inactive",
        "RESET_FILTER": "Reset Filter",
        "SYSTEM_USERS": "System Users",
        "ACTIVE_USERS": "Active Users",
        "INACTIVE_USERS": "Inactive Users"
    },
    "USER_DETAILS":{
        "ACTIVE":"Active",
        "INACTIVE":"Inactive",
        "BASIC_INFORMATION":"Basic Information",
        "CONTACT":"Contact",
        "EMAIL":"Email",
        "OTHER_INFORMATION":"Other Information",
        "DATE_OF_BIRTH":"Date of Birth",
        "EDIT_PROFILE":"Edit Profile",
        "LAST_LOGGED_IN":"Last Logged In",
        "USER_UPDATED_SUCCESSFULLY":"User Updated Successfully",
        "ACCOUNT_IS_NOT_VERIFIED_THUS_USER_CANNOT_BE_ACTIVATED":"Account is not verified. Thus, user can not be activated",
        "USER_NOT_FOUND":"User Not Found",
        "ROLES":"Roles"
    },
    "USER_AVATAR_UPLOADER": {
        "UPLOAD": "Upload",
        "PROFILE_PHOTO": "Profile Photo"
    },
    "ROLE_LIST":{

        "CREATE_ROLE": "Create Role",
        "ROLES": "Roles"
    },
    "ROLE_DETAILS":{
        "EDIT_ROLE": "Edit Role",
        "PERMISSIONS": "Permissions",
        "ASSIGNED_USERS":"Assigned Users",
        "No_USER_ASSIGNED":"No users has been assigned for this role yet"
    },
    "ROLE_CREATE":{
        "CREATE_ROLE":"Create Role",
        "EDIT_ROLE":"Edit Role",
        "NAME": "Name",
        "NAME_OF_ROLE":"Name of Role",
        "DESCRIPTION":"Description",
        "SHORT_DESCRIPTION":"Short Description",
        "SELECT_PERMISSIONS":"Select Permissions",
        "SEARCH":"Search",
        "PERMISSIONS":"Permissions",
        "YOUR_SELECTED_PERMISSIONS_WILL_APPEAR_HERE":"Your Selected permissions will appear here",
        "CANCEL":"Cancel",
        "UPDATE":"Update",
        "ROLE_NAME_VALIDATION_ERROR":"Role Name only contains lowercase letters without spaces",
        "ROLE_DESCRIPTION_VALIDATION_ERROR":"Role Description only contains letters and spaces",
        "ROLE_CREATED_SUCCESSFULLY": "Role Created Successfully",
        "ROLE_UPDATED_SUCCESSFULLY": "Role Updated Successfully",
        "ERROR_OCCURED_DURING_THE_OPERATION": "Error occured during the operation"
    },
    "PRODUCT":{
        "BASIC_INFO":"Basic Info",
        "FINANCIAL_INFO":"Financial Info",
        "MANUFACTURE_INFO":"Manufacture Info",
        "OTHER_INFO":"Other Info",
        "PRODUCT_DESCRIPTION":"Product Description",
        "VENDOR":"Vendor",
        "WAREHOUSE":"Warehouse",
        "PRODUCT_SIZE":"Product Size",
        "SIZE_UNIT":"Size Unit",
        "COLOUR":"Colour",
        "COLOUR_FAMILY":"Colour Family",
        "CATEGORY":"Category",
        "SUB_CATEGORY":"Sub-Category",
        "GILLETTE":"Gillette",
        "COST_PROCE":"Cost Price",
        "TAX_RATE":"Tax Rate",
        "VAT":"Vat",
        "SUPPLEMENTARY_DUTY":"Supplementary Duty (SD)",
        "ADVANCE_INCOME_TAX":"Advance Income Tax (AIT)",
        "RETAIL_PRICE":"Retail Price",
        "MODEL_NAME":"Model Name",
        "MODEL_NUMMBER":"Model Number",
        "SERIAL_NO":"Serial No",
        "BATCH_NO":"Batch No",
        "EXPIRE_DATE":"Expire Date",
        "MANUFACTURE_DATE":"Manufacturing Date",
        "RESTOCK_DATE":"Restock Date",
        "QUANTITY":"Quantity",
        "SKU":"SKU",
        "COUNTRY_OF_ORIGIN":"Country of Origin",
        "RETURN_POLICY":"Return Policy",
        "COMPILE_INFORMATION":"Compliance Information",
        "COST_PRICE":"Cost Price"
    },
    "DATE_PICKER":{
        "CANCEL":"Cancel",
        "SELECT":"Select"
    },
    "WAREHOUSE":{
        "WAREHOUSE_COORDINATES":"Warehouse Coordinates",
        "ZIP_CODE":"Zip Code",
        "METROPOLITAN_CITY":"Metropolitan City",
        "SPECIAL_CITY":"Special City",
        "SPECIAL_SELF_GOVERNING_CITY":"Special Self Governing City",
        "PROVIDANCE":"Providance",
        "CITY":"City",
        "COUNTRY":"Country",
        "DISTRICT":"District",
        "TOWN":"Town",
        "TOWNSHIP":"Township",
        "NEIGHBORHOOD":"Neighborhood",
        "VILLAGES":"Villages"
    },
    "CATEGORY_TREE": {
        "ALL_CATEGORY_TREE": "All Category Tree",
        "LOAD_MORE": "Load More...",
        "ADD_NEW_CATEGORY": "Add New Category"
    },
    "CATEGORY_DETAILS": {
        "SHOW_MORE": "Show More...",
        "CODE": "Code-",
        "EDIT_CATEGORY": "Edit Category",
        "DESCRIPTION": "Category Description",
        "PARENT": "Parent Category",
        "CHILD": "Child Category"
    },
    "CATEGORY_DIALOG": {
        "DISCARD": "Discard",
        "YES": "Yes"
    },
    "CATEGORY_CREATE": {
        "ADD_NEW_CATEGORY" : "Add new category",
        "EDIT_CATEGORY" : "Edit category",
        "CATEGORY_NAME" : "Category Name",
        "PARENT_CATEGORY" : "Parent Category",
        "SELECT_PARENT" : "Select Parent Category",
        "DESCRIPTION" : "Category Description",
        "CANCEL" : "Cancel",
        "ADD_CATEGORY" : "Add Category",
        "Edit_CATEGORY" : "Edit Category",
        "CATEGORY_OWN_PARENT" : "Category can not be own parent",
        "Child_CATEGORY_OWN_PARENT" : "Child category can not be a parent",
        "ERROR_UPLOADING_CATEGORY_PICTURE": "Error Uploading Category Picture",
        "CATEGORY_NAME_REQUIRED": "Category name is required",
        "CATEGORY_NAME_EXIST": "Category name already Exists",
        "CATEGORY_NAME_MINLENGTH": "Category name should be at least 1 character",
        "CATEGORY_NAME_MAXLENGTH": "Category name should be at most 50 character",
        "CATEGORY_NAME_PATTERN": "Category name should contain only letters and number. '.' and spaces are allowed except first position",
        "CATEGORY_DESCRIPTION_MAXLENGTH": "Category description should be at most 300 character"
    },
    "CATEGORY_AVATAR_UPLOADER": {
        "UPLOAD": "Upload"
    },
    "WAREHOUSE_LIST":{
        "ALL_WAREHOUSE":"All Warehouse",
        "CITY":"City",
        "ALL_CITY":"All City",
        "RESET_FILTER":"Reset Filter"
    },
    "PRODUCT_LIST":{
        "ALL_PRODUCT":"All Products",
        "ALL_BRAND":"All Brand",
        "BRAND":"Brand",
        "ALL_SUBBRAND":"All Sub Brand",
        "SUBBRAND":"Sub Brand",
        "ALL_CATEGORY":"All Category",
        "CATEGORY":"Category",
        "DATEANDTIME_RANGE":"Date & Time Range"
    },
    "TOKEN_LIST":{
        "ALL_TOKEN":"All Token",
        "OFFLINE_TOKEN":"Offline Token",
        "LIVE_TOKEN":"Live Token",
        "SOULDOUT_TOKEN":"Sould Out Token",
        "RESET_FILTER":"Reset Filter",
        "DATEANDTIME_RANGE":"Date & Time Range"
    },
    "TOKEN_DETAIL":{
        "TOKEN_ID":"Token ID",
        "PRODUCT_ID":"Product ID",
        "QUANTITY_OF_TOKEN":"Quantity Of Token",
        "CATEGORY":"Category",
        "PER_TOKEN_PRICE":"Per Token Price",
        "MATURITY_DATE":"Maturity Date",
        "REDEMPTION_DELAY": "Redemption Delay",
        "OFF_LINE": "OFFLINE",
        "LIVE": "LIVE",
        "MAKE_TOKEN_LIVE":"Make Token Live",
        "MAKE_TOKEN_OFFLINE":"Make Token Ofline",
        "TOKEN_LIVED":"Token Lived Successfully",
        "BASIC_INFO": "Basic Info",
        "FINANCIAL_INFO": "Financial Info",
        "MANUFACTURE_INFO": "Manufacture Info",
        "OTHER_INFO": "Other Info",
        "MEDIA_CONTENT": "Media Content",
        "QUOTA": "Quota",
        "TOKEN_INFO": "Token Info",
        "OWNERS_INFO": "Owner's Info",
        "LOG_INFO": "Log Info"
    },
    "INVENTORY_TABLE": {
        "VIEW": "View",
        "ID": "ID",
        "PRODUCT_NAME": "PRODUCT NAME",
        "TIME_OF_ARRIVAL": "TIME OF ARRIVAL",
        "MODEL_NUMBER": "MODEL NUMBER",
        "BRAND": "BRAND",
        "SUB_BRAND": "SUB BRAND",
        "COLOUR": "COLOUR",
        "QUANTITY": "QUANTITY",
        "WAREHOUSE": "WAREHOUSE",
        "TAX": "TAX",
        "VAT": "VAT",
        "SD": "SD",
        "AIT": "ALT",
        "RETAIL_PRICE": "RETAIL PRICE",
        "EXPIRY_DATE": "EXPIRY DATE",
        "WAREHOUSE_NAME": "WAREHOUSE NAME",
        "COORDINATES": "COORDINATES",
        "ADDRESS": "ADDRESS",
        "ZIP_CODE": "ZIP CODE",
        "CITY": "CITY"
    },
    "ROLE_TABLE": {
        "VIEW_DETAILS": "View Details",
        "EDIT": "Edit",
        "USER_ROLE": "USER ROLE",
        "DESCRIPTION": "DESCRIPTION"
    },
    "TOKEN_TABLE": {
        "VIEW": "View",
        "NOT_ASSIGNED": "NOT ASSIGNED",
        "OFFLINE_TOKEN": "Offline Token",
        "LIVE_TOKEN": "Live Token",
        "SOLD_OUT_TOKEN": "Sold Out Token",
        "TOKENIZED_ON": "TOKENIZED ON",
        "TOKEN_ID": "TOKEN ID",
        "TOKEN_NAME": "TOKEN NAME",
        "CATEGORY": "CATEGORY",
        "PRODUCT_ID": "PRODUCT ID",
        "TOTAL_QUANTITY": "TOTAL QUANTITY",
        "SOLD_QUANTITY": "SOLD QUANTITY",
        "MATURITY": "MATURITY"
    }

}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"TranslateKey.json"
translate_client=translate.Client()

#print((translate_client.translate('Hello',"Ko"))['translatedText'])

def translate(en_dict,lang):
    for key, value in en_dict.items():
        if type(value)==str:
            translated_value=(translate_client.translate(value,lang))
            translated_value=translated_value['translatedText']
            en_dict[key]=translated_value

        elif type(value)==dict:
            for k, v in value.items():
                t_value=(translate_client.translate(v,lang))
                t_value=t_value['translatedText']
                value[k]=t_value

            en_dict[key]=value
    filename=f"{lang}.json"    
    with open(filename, 'w', encoding='utf8') as json_file:
        json.dump(en_dict, json_file,indent=3, ensure_ascii=False)

translate(en_text,'ko')




print("--- %s seconds ---" % (time.time() - start_time))