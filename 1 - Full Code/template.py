from searcher import tfidfsearcher,bm25searcher
def mainpage():
    x=""
    x+="<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
    x+="<html xmlns=\"http://www.w3.org/1999/xhtml\">"
    x+="<head>"
    x+="<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\" />"
    x+="<!-- TemplateBeginEditable name=\"doctitle\" -->"
    x+="<title>Welcome To Legal Document Search Engine</title>"
    x+="<!-- TemplateEndEditable -->"
    x+="<!-- TemplateBeginEditable name=\"head\" -->"
    x+="<!-- TemplateEndEditable -->"
    x+="</head>"
    x+="<body>"
    x+="<p><a href=\"tfidf\">TF-IDF Search</a></p>"
    x+="<p><a href=\"bm25\">BM-25 Search</a> </p>"
    x+="</body>"
    x+="</html>"
    return x

def tfidfx(lig,page):
    x=""
    #x+="<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
    #x+="<html xmlns=\"http://www.w3.org/1999/xhtml\">"
    #x+="<head>"
    #x+="<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\" />"
    #x+="<!-- TemplateBeginEditable name=\"doctitle\" -->"
    #x+="<title>Welcome To Legal Document Search Engine</title>"
    #x+="<!-- TemplateEndEditable -->"
    #x+="<!-- TemplateBeginEditable name=\"head\" -->"
    #x+="<!-- TemplateEndEditable -->"
    #x+="</head>"
    #x+="<body>"
    x+="<form id=\"form1\" name=\"form1\" method=\"post\" action=\"\">"
    x+="<label>Search:"
    x+="<input type=\"text\" name=\"textfield\" style=\"width:80%\" value=\""+lig+"\"/>"
    x+="</label>"
    x+="<input name=\"search\" type=\"submit\" id=\"search\" value=\"Search\" />"
    if(lig!=""):
        x+="<table width=\"100%\" border=\"0\">"
        x+="<tr>"
        x+="<td width='59%'>"
        page = page.replace("Next ","")
        page = page.replace("Previous ","")
        if "Search" in str(page) or str(page)==0:
            page = "1"
            print("Page Converted To 1")
        x+=tfidfsearcher(lig,int(page))
        #x+="</td>"
        #x+="<td rowspan=\"2\" width=\"100%\" align=\"left\" valign=\"top\">Image Graph </td>"
        x+="</tr>"
        x+="<tr>"
        next_value = ""
        prev_value = ""
        prev_enabled=""
        next_enabled=""
        if page=="1":
            prev_enabled="disabled"
        if page=="10":
            next_enabled="disabled"
        if int(page)<=10 and int(page)>=1:
            prev_value = str(int(page)-1)
            next_value = str(int(page)+1)
        x+="<td><b>Pages:</b><input name=\"search\" type=\"submit\" id=\"search\" value=\"Previous "+str(prev_value)+"\" "+prev_enabled+"/> <input name=\"search\" type=\"submit\" id=\"search\" value=\"1\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"2\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"3\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"4\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"5\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"6\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"7\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"8\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"9\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"10\" /><input name=\"search\" type=\"submit\" id=\"search\" value=\"Next "+str(next_value)+"\" "+next_enabled+" /></td>"
        x+="</tr>"
        x+="</table>"
        #x+=page
    x+="</form>"
    #x+="</body>"
    #x+="</html>"
    return x

def bm25x(lig,page):
    x=""
    #x+="<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
    #x+="<html xmlns=\"http://www.w3.org/1999/xhtml\">"
    #x+="<head>"
    #x+="<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\" />"
    #x+="<!-- TemplateBeginEditable name=\"doctitle\" -->"
    #x+="<title>Welcome To Legal Document Search Engine</title>"
    #x+="<!-- TemplateEndEditable -->"
    #x+="<!-- TemplateBeginEditable name=\"head\" -->"
    #x+="<!-- TemplateEndEditable -->"
    #x+="</head>"
    #x+="<body>"
    x+="<form id=\"form1\" name=\"form1\" method=\"post\" action=\"\">"
    x+="<label>Search:"
    x+="<input type=\"text\" name=\"textfield\" style=\"width:80%\" value=\""+lig+"\"/>"
    x+="</label>"
    x+="<input name=\"search\" type=\"submit\" id=\"search\" value=\"Search\" />"
    if(lig!=""):
        x+="<table width=\"100%\" border=\"0\">"
        x+="<tr>"
        x+="<td width='59%'>"
        if "Search" in str(page):
            page = "1"
            print("Page Converted To 1")
        x+=bm25searcher(lig,int(page))
        #x+="</td>"
        #x+="<td rowspan=\"2\" width=\"100%\" align=\"left\" valign=\"top\">Image Graph </td>"
        x+="</tr>"
        x+="<tr>"
        next_value = ""
        prev_value = ""
        prev_enabled=""
        next_enabled=""
        if page=="1":
            prev_enabled="disabled"
        if page=="10":
            next_enabled="disabled"
        if int(page)<=10 and int(page)>=1:
            prev_value = str(int(page)-1)
            next_value = str(int(page)+1)
        x+="<td><b>Pages:</b><input name=\"search\" type=\"submit\" id=\"search\" value=\"Previous "+str(prev_value)+"\" "+prev_enabled+"/> <input name=\"search\" type=\"submit\" id=\"search\" value=\"1\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"2\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"3\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"4\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"5\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"6\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"7\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"8\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"9\" /> <input name=\"search\" type=\"submit\" id=\"search\" value=\"10\" /><input name=\"search\" type=\"submit\" id=\"search\" value=\"Next "+str(next_value)+"\" "+next_enabled+" /></td>"
        x+="</tr>"
        x+="</table>"
        #x+=page
    x+="</form>"
    #x+="</body>"
    #x+="</html>"
    return x