class EmailConstants:    subject = "Subject"    From = "From"    to = "To"    cc = "Cc"    smtp_server = "smtp.gmail.com"    alternative = "alternative"    plain = "plain"    mail_subject = " "    mail_content = " "class Collections:    users = "users"class ResponseMessage:    @staticmethod    def final_json(status, message, data):        if data is None:            json = {"status": status, "message": message, "data": {}}        else:            json = {"status": status, "message": message, "data": data}        return jsonclass ResponseStatus:    success = "success"    failure = "failure"class FinalJson:    status = "status"    message = "message"    data = "data"