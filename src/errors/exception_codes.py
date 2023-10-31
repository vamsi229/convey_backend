class MongoExceptionCodes:
    MONGO001 = (
        "Error Code MONGO001: Server was unable to establish connection with MongoDB"
    )
    MONGO002 = "Error Code MONGO002: Server faced a problem when inserting document(s) into MongoDB"
    MONGO003 = "Error Code MONGO003: Server faced a problem to find the document(s) with the given condition"
    MONGO004 = "Error Code MONGO004: Server faced a problem to delete the document(s) with the given condition"
    MONGO005 = "Error Code MONGO005: Server faced a problem to update the document(s) with the given condition and data"
    MONGO006 = "Error Code MONGO006: Server faced a problem when aggregating the data"
    MONGO007 = (
        "Error Code MONGO007: Server faced a problem when closing MongoDB connection"
    )
    MONGO008 = (
        "Error Code MONGO008: Found an existing record with the same ID in MongoDB"
    )
    MONGO009 = "Error Code MONGO009: Server faced a problem when fetching distinct documents from MongoDB"
    MONGO010 = "Error Code MONGO010: Server faced a problem when performing a search and replace in MongoDB"
    MONGO011 = (
        "Error Code MONGO011: Server faced a problem when de-serializing MongoDB object"
    )


class ValidationExceptions:
    IL001 = "Error Code IL001: Required Keys are missing!"
    IL002 = "Error Code IL002: User id is missing in the cookies!"


class MetadataExceptionCodes:
    SERV001 = "Server did not get a successful response. Check the server logs for more information"
    SERV002 = (
        "Server faced a problem when processing the service. "
        "Check the server logs or contact administrator for more information"
    )


class SiteExceptionCodes:
    ST001 = "Error Code ST001: Required fields were missing"
    ST002 = "Error Code ST002: Server failed to make site upload template"
    ST003 = "Error Code ST003: Invalid customer project template found,Please contact support team!"
    ST004 = "Error Code ST004: Server failed to provide preview of uploaded file"
    ST005 = "Error Code ST005: Uploaded file extension is not specified"
    ST006 = "Error Code ST006: Required column names were altered "
    ST007 = "Error Code ST007: Unauthorized project details "
    ST008 = "Error Code ST008: Site Name should not be empty "
    ST009 = "Error Code ST009: Department Name should not be empty "
    ST010 = "Error Code ST010: Line Name should not be empty "
    ST011 = "Error Code ST011: Equipment Name should not be empty "
    ST012 = "Error Code ST012: Duplicate site name found within sheet "
    ST013 = "Error Code ST013: Duplicate department name found "
    ST014 = "Error Code ST014: Duplicate line name found "
    ST015 = "Error Code ST015: Duplicate equipment name found "
    ST016 = "Error Code ST016: Site name already exists in iLens platform "
    ST017 = "Error Code ST017: Site name found other than specified in site information"
    ST018 = "Error Code ST018: Department name found other than specified in department information"
    ST019 = "Error Code ST019: Line name found other than specified in line information"

CAI_RE_000 = "PYTHON RELATED ERROR"


CAI_RE_001 = "Cannot able to establish Database connection"
CAI_RE_002 = "Error in insertion of data in Postgre"
CAI_RE_003 = "Error in finding of data in Postgre"
CAI_RE_004 = "Error in deleting of data in Postgre"
CAI_RE_005 = "Error while updation of data in Postgre"
CAI_RE_006 = "Error in Executing query"
CAI_RE_007 = "Error while Executing SELECT query !"
CAI_RE_008 = "Error while fetching all records with condition"
CAI_RE_009 = "Error while fetching specified records with condition"
CAI_RE_010 = "Error while fetching specified columns"
CAI_RE_011 = "Error in closing of Postgre connection"


CAI_RE_101 = "{0} is not present in JSON"
CAI_RE_102 = "No data found"
CAI_RE_103 = "'{0}' already exists!"
CAI_RE_104 = "Cannot execute Linux based commands"
CAI_RE_105 = "Cannot create file {0}"
CAI_RE_106 = ""
CAI_RE_107 = "No dataset is selected for the project"
CAI_RE_108 = "Error while uploading File"
CAI_RE_109 = "Error while Downloading file"
CAI_RE_110 = "Problem in uploading data file to AZURE"
CAI_RE_111 = "please attach any file first"
CAI_RE_112 = "File size exceeding"
CAI_RE_113 = "Wrong option chosen {0}"
CAI_RE_114 = "Missing '{}' in request headers"
CAI_RE_115 = "{} not exist. Enter valid data"
CAI_RE_116 = "no filename is there"
