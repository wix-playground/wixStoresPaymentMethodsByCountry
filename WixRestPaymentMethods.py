#!python
#Supported Payment Methods by Country - Wix Restaurants
#by Michael Salaverry
#MichaelS@wix.com

#Payment methods go here and = countries that they support
PayPal = "United Kingdom, United States, Canada"
Authorize = "Andorra, Austria, Australia, Belgium, Canada, Switzerland, Cyprus, Czech Republic, Germany, Denmark, Spain, Finland, France, United Kingdom, Gibraltar, Greece, Hungary, Ireland, Italy, Liechtenstein, Luxembourg, Monaco, Malta, Netherlands, Norway, New Zealand, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia, San Marino, United States, Holy See (Vatican City State)"
Stripe = "Austria, Australia, Belgium, Canada, Switzerland, Germany, Denmark, Spain, Finland, France, United Kingdom, Ireland, Japan, Italy, Luxembourg, Mexico, Netherlands, Norway, Sweden, United States"
PaymentExpress = "Australia, Bangladesh, Brunei, Canada, United Kingdom, Hong Kong, Ireland, India, Macau, Malaysia, New Zealand, Singapore, United States, South Africa"
WorldPay = "Belgium, Switzerland, Germany, Denmark, Spain, Finland, France, United Kingdom, Hong Kong, Ireland, Italy, Luxembourg, Netherlands, Norway, Sweden, Singapore, United States"
eWay = "Australia, Hong Kong, Malaysia, New Zealand, Singapore"
Braintree = "Andorra, Austria, Australia, Belgium, Bulgaria, Canada, Switzerland, Cyprus, Czech Republic, Germany, Denmark, Estonia, Spain, Finland, France, United Kingdom, Guernsey, Gibraltar, Greece, Hong Kong, Croatia, Hungary, Ireland, Isle of Man, Iceland, Italy, Jersey, Liechtenstein, Lithuania, Luxembourg, Latvia, Monaco, Malta, Malaysia, Netherlands, Norway, New Zealand, Poland, Portugal, Romania, Sweden, Singapore, Slovenia, Slovakia, San Marino, Turkey, United States"
MercadoPago = "Argentina, Brazil, Chile, Colombia, Mexico, Venezuela"
PayBox = "Belgium, France, Netherlands"
Mercury = ['United States']
FatZebra = ['Australia']
DengiOnline = ['Russia']
Tranzila = ['Israel']
PeleCard = ['Israel']
CreditGuard = ['Israel']
PagueloFacil = ['Panama']


paymentmethods = [PayPal,Authorize,Stripe,PaymentExpress,WorldPay,eWay,Braintree,MercadoPago,PayBox,Mercury,FatZebra,DengiOnline,Tranzila,PeleCard,CreditGuard,PagueloFacil]
#convert all strings to lists
i = 0
for i in range(0,9):
    paymentmethods[i] = paymentmethods[i].split(", ")

for i in range(9,15):
    paymentmethods[i] = paymentmethods[i]

countries = []

for i in range (0,15):
    paymentmethods[i] = list(paymentmethods[i])
    countries += paymentmethods[i]


countries = sorted(countries)

#this code prevents duplicates
country = []
i=0
for i in range(0,len(countries)):
    if countries[i] not in country:
        country.append(countries[i])

#This following part makes a paymentmethods list 
#this line is for the HTML table labels - includes links to each payment method
paymentmethodsnames = ['PayPal','Authorize','Stripe','PaymentExpress','WorldPay','eWay','Braintree','MercadoPago','PayBox','Mercury','FatZebra','DengiOnline','Tranzila','PeleCard','CreditGuard','PagueloFacil']

x=0
z=0
with open("wspmrest.html", "w") as wspm:
    print('<html><body><style>body{font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}</style>',file=wspm)
    print("Please select your country below to see our supported payment methods for Wix Restaurants: <br><br>",file=wspm)
    #generates the dropdown menu of all the countries we support
    print('<select id="selectedcountry" onchange="optionCheck()">',file=wspm)
    for z in range(0,len(country)):
            print('<option value="',z,'">',country[z],'</option>',file=wspm)
    print('</select><br><br>',file=wspm)
    #styling options
    print("",file=wspm)
    print("""<style>
    table{
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 100%;
    }
    td {
        text-align: center;
        padding: 5px;
        border-radius: 10px;
        border:1px solid #3ba561;
        background: #65c888;
    }
    th {
        text-align: left;
    }
    td.supported{background: #65c888;}
    td.notsupported{background: red;}
    </style>""",file=wspm)
    #current approach: hide everything till the select menu reveals it
    #generates a bunch of not displayed tables for each country
    for z in range(0,len(country)):#each country
        print('<table style="display:none;" id="',z,'">',file=wspm) #use single and double quotes together to escape them
        print('<th colspan="2">',country[z],'</th>',file=wspm) #print country name
        #print("<br>",file=wspm)
        for x in range(0,len(paymentmethodsnames)):#each payment method
            if country[z] in paymentmethods[x]:
                print('<tr><td>',paymentmethodsnames[x],'</td><td class="supported"> Supported </td></tr>',file=wspm)
            else: print('<tr><td>',paymentmethodsnames[x],'</td><td class="notsupported"> Not Supported</td></tr>',file=wspm) #print current payment supported or not
        #,paymentmethodsnames[x]
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
    print("<br>Third-party restrictions and limitations may apply.<br>If you don't see your country, or you have any feedback or questions, contact us</body></html>",file=wspm)

