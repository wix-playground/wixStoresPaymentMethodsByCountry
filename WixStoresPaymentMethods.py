#python
#pay method by country module

#Payment methods go here and = countries that they support
PayPal = "Algeria,Angola,Benin,Botswana,Burkina Faso,Burundi,Cameroon,Cape Verde,Chad,Comoros,Cote d Ivoire,Democratic Republic of the Congo,Djibouti,Egypt,Eritrea,Ethiopia,Gabon Republic,Gambia,Guinea,Guinea-Bissau,Kenya,Lesotho,Madagascar,Malawi,Mali,Mauritania,Mauritius,Mayotte,Morocco,Mozambique,Namibia,Niger,Nigeria,Republic of the Congo,Reunion,Rwanda,Saint Helena,Sao Tome and Principe,Senegal,Seychelles,Sierra Leone,Somalia,South Africa,Swaziland,Tanzania,Togo,Tunisia,Uganda,Zambia,Zimbabwe,Anguilla,Antigua and Barbuda,Argentina,Aruba,Bahamas,Barbados,Belize,Bermuda,Bolivia,Brazil,British Virgin Islands,Canada,Cayman Islands,Chile,Colombia,Costa Rica,Dominica,Dominican Republic,Ecuador,El Salvador,Falkland Islands,French Guiana,Greenland,Grenada,Guadeloupe,Guatemala,Guyana,Honduras,Jamaica,Martinique,Mexico,Montserrat,Netherlands Antilles,Nicaragua,Panama,Paraguay,Peru,Saint Kitts and Nevis,Saint Lucia,Saint Pierre and Miquelon,Saint Vincent and the Grenadines,Suriname,Trinidad and Tobago,Turks and Caicos,United States,Uruguay,Venezuela,Armenia,Australia,Bahrain,Bhutan,Brunei,Cambodia,China,Cook Islands,Fiji,French Polynesia,Hong Kong,India,Indonesia,Israel,Japan,Jordan,Kazakhstan,Kiribati,Kuwait,Kyrgyzstan,Laos,Malaysia,Maldives,Marshall Islands,Federated States of Micronesia,Mongolia,Nauru,Nepal,New Caledonia,New Zealand,Niue,Norfolk Island,Oman,Palau,Papua New Guinea,Philippines,Pitcairn Islands,Qatar,Samoa,Saudi Arabia,Singapore,Solomon Islands,South Korea,Sri Lanka,Taiwan,Tajikistan,Thailand,Tonga,Turkmenistan,Tuvalu,United Arab Emirates,Vanuatu,Vietnam,Wallis and Futuna,Yemen,Albania,Andorra,Austria,Azerbaijan Republic,Belarus,Belgium,Bosnia and Herzegovina,Bulgaria,Croatia,Cyprus,Czech Republic,Denmark,Estonia,Faroe Islands,Finland,France,Georgia,Germany,Gibraltar,Greece,Hungary,Iceland,Ireland,Italy,Latvia,Liechtenstein,Lithuania,Luxembourg,Macedonia,Malta,Moldova,Monaco,Montenegro,Netherlands,Norway,Poland,Portugal,Romania,Russia,San Marino,Serbia,Slovakia,Slovenia,Spain,Svalbard and Jan Mayen,Sweden,Switzerland,Ukraine,United Kingdom,Vatican City"
Moolah = "Andorra, Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Liectenstein, Luxembourg, Malta, Monaco, The Netherlands, Norway, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, Spain, Sweden, Switzerland, Vatican City, United States, Canada, United Kingdom, Australia"
Stripe = "Austria, Australia, Belgium, Canada, Germany, Denmark, Spain, France, United Kingdom, Ireland, Italy, Luxembourg, The Netherlands, Norway, Sweden, United States, Japan"
MercadoPago = "Argentina, Brazil, Colombia, Mexico, Venezuela, Chile"
Wirecard = "Andorra, Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Isle of Man, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Monaco, Netherlands, Norway, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, United Kingdom, Vatican City"
PagSeguro = ['Brazil']
Offline = ['Other Country']#["Other Country"]

paymentmethods = [PayPal,Moolah,Stripe,MercadoPago,Wirecard,PagSeguro,Offline]
#convert all strings to lists
PayPal = paymentmethods[0].split(",")
Moolah = paymentmethods[1].split(", ")
Stripe = paymentmethods[2].split(", ")
MercadoPago = paymentmethods[3].split(", ")
Wirecard = paymentmethods[4].split(", ")
PagSeguro = paymentmethods[5]
Offline = paymentmethods[6]

#this part generates a list of all the countries we support for looping
countries = PayPal+Moolah+Stripe+MercadoPago+Wirecard+PagSeguro
countries = sorted(countries)
#this code prevents duplicates
country = []
i=0
for i in range(0,len(countries)):
    if countries[i] not in country:
        country.append(countries[i])

paymentmethods[6] = countries #adds every country to offline payment section

#This following part makes a paymentmethods list 
#this line is for the HTML table labels - perhaps I should put in links to each payment method
paymentmethodsnames = ["PayPal","Moolah","Stripe","MercadoPago","Wirecard","PagSeguro","Offline"]


###Debug the offline payments section
##print("Supported" if country[68] in paymentmethods[6] else "no")
##print(country[68])
##print(paymentmethods[6])

x=0
z=0
with open("wspm.html", "w") as wspm:
    print("<html>",file=wspm)
    print("Select a country to view the supported payment methods: <br><br>",file=wspm)
    #generates the dropdown menu of all the countries we support
    print('<select id="selectedcountry" onchange="optionCheck()">',file=wspm)
    for z in range(0,len(country)):
            print('<option value="',z,'">',country[z],'</option>',file=wspm)
    print('</select><br><br>',file=wspm)
    #styling options
    print("",file=wspm)
    print("""<style>
    table{
        width:100%;
        border:1px solid black;
        font-size: 100%;
    }
    td {
        text-align: center;
        border:1px solid black;
    }
    </style>""",file=wspm)
    #current approach: hide everything till the select menu reveals it
    #generates a bunch of not displayed tables for each country
    for z in range(0,len(country)):#each country
        print('<table style="display:none;" id="',z,'">',file=wspm) #use single and double quotes together to escape them
        print('<th>',country[z],'</th>',file=wspm) #print country name
        print("<tr>",file=wspm)
        for x in range(0,len(paymentmethodsnames)):#each payment method
            print("<td>",paymentmethodsnames[x],"<br>","Supported" if country[z] in paymentmethods[x] else "Not Supported","</td>",file=wspm) #print current payment supported or not
        print("</tr>",file=wspm)
        print("</table>",file=wspm)

    #reveal table using javascript - brute force style
    print("""
    <script>
    function optionCheck(){
            var option = document.getElementById("selectedcountry").value;""",file=wspm)
    for z in range(0,len(country)):
         print('        document.getElementById("',z,'").style.display ="none";',file=wspm)
            
    print("""        document.getElementById(option).style.display ="block";
            }
    </script>
    """,file=wspm)
    print("</html>",file=wspm)

