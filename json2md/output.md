---

title: LotteryStore-PRODUCTION

language_tabs:
  - shell

toc_footers:
 - <a href='https://github.com/accubits'>Documentation Powered by Accubits</a>

search: true

---

# Introduction

MyLotteryStore API'S list for both admin and users with detailed description and values.

# admin

## userList

List the entire users in the platform

### HTTP request

`GET {{URL}}/admin/userList?pageNumber=1&limit=2&searchQuery`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### Query Params

|Parameter|Description|Value|
|---|---|---|
|pageNumber|Page to be displayed|1|
|limit|Limit to be displayed|2|
|searchQuery|First name of the user||

## userContestResults

Displaying the contests participants details

### HTTP request

`GET {{URL}}/admin/userContestResults?id=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### Query Params

|Parameter|Description|Value|
|---|---|---|
|id||1|

## getUserWalletTransactions

Get all the wallet transactions of individual users

### HTTP request

`GET {{URL}}/admin/getUserWalletTransactions?page=1&limit=100&userId=4&date=2019-10-03&status=1`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|page|Page number to be dislayed|1|
|limit|Limit of the details per page|100|
|userId|Id of the user|4|
|date|optional; Transaction date of the ticket (date in UTC)|2019-10-03|
|status|optional;Status of the wallet transactions(|1|

## adminLogout

Logout of admin

### HTTP request

`GET {{URL}}/admin/adminLogout`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getPowerballPrizeWinners

Get the details of powerball winners

### HTTP request

`POST {{URL}}/admin/getPowerballPrizeWinners`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|contestId|Id of the contest|1|
|prizeType|Type of the prize
(
1:Jackpot amount of the contest
2: $1 Million
3:$50,000
4:$100
5:$100
6:$7
7:$7
8:$4
9:$4
)|6|
|query|Keyword to be searched(First name, last name and email id of the user)|name|
|page|Page number to be dispalyed|1|
|size|Limit of the details to be displayed per page|10|

## ongoingGamesList

Listing the ongoing games

### HTTP request

`GET {{URL}}/admin/ongoingGamesList`

## getEarningSummary

Get the summary of the earnings

### HTTP request

`GET {{URL}}/admin/getEarningSummary?year=2019`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|year|Year to get the earnings graph(YYYY)|2019|

## deleteUser

Delete a user from the platform

### HTTP request

`POST {{URL}}/admin/deleteUser`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|id|Id of the user to be deleted|24|

## usertransactionDetails

Get the transaction details of a user

### HTTP request

`GET {{URL}}/admin/usertransactionDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## recentGames

Listing the recent games

### HTTP request

`GET {{URL}}/admin/recentGames`

## removePowerballWinner

Changing the powerball winner

### HTTP request

`POST {{URL}}/admin/removePowerballWinner`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|winnerId|Id of the winner to be removed|35|
|contestId|Id of the contest|1|
|prizeType|Type of the prize
(
1:Jackpot amount of the contest
2: $1 Million
3:$50,000
4:$100
5:$100
6:$7
7:$7
8:$4
9:$4
)|6|

## removeContest

Remone the details of a contest

### HTTP request

`DELETE {{URL}}/admin/removeContest/6`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## Admin Login

Login for the admin

### HTTP request

`POST {{URL}}/admin/login`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|username|username of the admin|xxxx@xxxx.com|
|password|password of the admin|xxxxxxxxxxxxxxxxxxxxx|

## powerballParticipantsDetails

Listing the details of a powerball participants

### HTTP request

`GET {{URL}}/admin/powerballParticipantsDetails?contestId=29&searchQuery=name&pageNumber=1&limit=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### Query Params

|Parameter|Description|Value|
|---|---|---|
|contestId|Id of the contest|29|
|searchQuery|Keyword to be searched(first name or last name of the participant)|name|
|pageNumber|Page number to be dispalyed|1|
|limit|Limit of the details to be displayed per page|1|

## getPowerballDraftResult

Get the powerball game result

### HTTP request

`GET {{URL}}/admin/getPowerballDraftResult/1`

## updatePowerballResult

Updating the powerball results

### HTTP request

`POST {{URL}}/admin/updatePowerballResult`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|contestId|Id of the contest to be edited|1|
|whiteball1|Details to be updated in whiteball 1 in result|15|
|whiteball2|Details to be updated in whiteball 2 in result|19|
|whiteball3|Details to be updated in whiteball 3 in result|39|
|whiteball4|Details to be updated in whiteball 4 in result|47|
|whiteball5|Details to be updated in whiteball 5 in result|51|
|powerball|Details to be updated in powerball in result|16|

## getWalletTransactions

Get all the wallet transactions

### HTTP request

`GET {{URL}}/admin/getWalletTransactions?page=1&limit=10&date=2019-10-04&type=1&status=`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|page|Page number to be dislayed|1|
|limit|Limit of the details per page|10|
|date|Transaction date of the ticket (date in UTC)|2019-10-04|
|type|Type of wallet transactions(
1:Receive
2:Spend)|1|
|status|Status of the wallet transactions(
1:Processing
2:Success
3:Failed)||

## updateContestDetails

Updating the details of the contest

### HTTP request

`POST {{URL}}/admin/updateContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|contestId|Id of the contest to be updated|15|
|startsDate|Start date of the contest (date in UTC)|2019-10-16 13:57:00|
|drawDate|Draw date of the contest (date in UTC)|2019-10-21 13:57:00|
|jackpot|Jackpot amount for the contest|200000|
|status|Status of the contest
(0:Inactive,
1:Active)|1|
|ticketAmount|Amount of the ticket|2|
|isPowerPlay|Powerplay status(true or false)|true|
|powerPlayTicketAmount|Amount of the powerplay ;Optional (If isPowerPlay is true) |3232|

## getWalletOverview

Get the overview of the wallet

### HTTP request

`GET {{URL}}/admin/getWalletOverview`

## getTransactions

Get all the transaction details

### HTTP request

`GET {{URL}}/admin/getTransactions?page=1&limit=100&date=2019-10-04&status=5`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|page|Page number to be dislayed|1|
|limit|Limit of the details per page|100|
|date|Transaction date of the ticket (date in UTC)|2019-10-04|
|status|Status of the transactions(
1:Initiated
2:Processing
3:Success
4:Rejected
5:Dispute)|5|

## getWalletBalance

Get the wallet balance of admin

### HTTP request

`GET {{URL}}/admin/getWalletBalance?userId=1`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|userId|Id of the user|1|

## getAllContestDetails

Get all the contest details

### HTTP request

`POST {{URL}}/admin/getAllContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|page|Page number to be displayed|1|
|size|Limit of the details displayed per page|10|
|gameType|Type of the game to be played (! for powerball) |1|
|isPowerPlay|optional; Powerplay status(true or false)|N|
|drawDate|optional  Draw date of the contest (date in UTC format(YYYY-MM-DD))|2019-11-02|

## getContestDetails

Get the details of a contest

### HTTP request

`POST {{URL}}/admin/getContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|contestId|Id of the contest|1|

## publishPowerballResult

Publish the powerball result

### HTTP request

`POST {{URL}}/admin/publishPowerballResult`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|contestId|Id of the contest to be published|1|

## viewUser

Display the details of a particular user

### HTTP request

`GET {{URL}}/admin/viewUser?id=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### Query Params

|Parameter|Description|Value|
|---|---|---|
|id|Id of the user|1|

## blockUser

Blocking a user from platform

### HTTP request

`POST {{URL}}/admin/blockUser`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|id|Id of the user to be blocked|12|

## getParticipantsDetailsToCsv

Get all the participants of a contest in csv format

### HTTP request

`GET {{URL}}/admin/getParticipantsDetailsToCsv?contestId=103`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|contestId|Id of the contest|103|

## getUserTransactions

Get all the user transactions

### HTTP request

`GET {{URL}}/admin/getUserTransactions?page=1&limit=10&userId=4`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|page|Page number to be dislayed|1|
|limit|Limit of the details per page|10|
|userId|Id of the user|4|

## userUnBlock

Unblock a blocked user

### HTTP request

`POST {{URL}}/admin/userUnBlock`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|id|Id of the user to be unBlocked|10|

## setContestDetails

Setting the contest details of the game

### HTTP request

`POST {{URL}}/admin/setContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|gameType|Type of the game to be played (! for powerball)|1|
|startsDate|Start date of the contest (date in UTC)|2019-10-28 13:57:00|
|drawDate|Draw date of the contest (date in UTC)|2019-11-25 13:57:00|
|jackpot|Jackpot amount for the contest|200000|
|status|Status of the contest
(0:Inactive,
1:Active)|1|
|ticketAmount|Amount of the ticket|2|
|isPowerPlay|Powerplay status(true or false)|true|
|powerPlayTicketAmount|Amount of the powerplay ;Optional (If isPowerPlay is true) |2|

## getPaymentOverview

Get the overview of the payments

### HTTP request

`GET {{URL}}/admin/getPaymentOverview`

# APIs

## userTicketResults

List the tickets taken for a game

### HTTP request

`GET {{URL}}/user/userTicketResults?pageNumber=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||C4xUel_FJ|

### Query Params

|Parameter|Description|Value|
|---|---|---|
|pageNumber|Page number to be displayed|1|

## getWinnerSummary

Get the winners summary

### HTTP request

`GET {{URL}}/games/getWinnerSummary/1`

## getTransactionHistory

Get the transaction history of the user

### HTTP request

`POST {{URL}}/user/getTransactionHistory`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|page|Page number to be diaplayed|1|
|size|Limit of the  details to be displayed|10|

## registration

Registeration page of the user

### HTTP request

`POST {{URL}}/user/registration`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|emailId|Email of the user for login|sijojmvcb@accubits.com|
|firstName|First name of the user (Maximun length 50 characters)|qwertyu|
|lastName|Last name of the user(Maximun length 50 characters)|v p|
|dob|Date of birth of the user|2001-04-04|
|phoneNo|Phone number of the user (Minimum length is 10 and maximum length is 20)|12345678901234567890|
|affiliateCode|Affiliate code of the user if exists|test|
|password|Password of the user for login|sijo1234S!|
|country|Country of the user(Drop down)|1|
|state|State of the user (Maximun length 50 characters)|qwertyui|
|city|City of the user (Maximun length 50 characters)|qwerty|
|zip|Zip code of the user(Maximun length 50 characters)|1234567|
|streetAddress|Street address of the user(Maximun length 100 characters)|qwertyu|

## getWalletHistory

Get the wallet history of the user

### HTTP request

`POST {{URL}}/user/getWalletHistory`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|page|Page number to be displayed|1|
|size|Limit of the details to be displayed|10|

## makeWalletPayment

Make the payment for the game

### HTTP request

`POST {{URL}}/payment/makeWalletPayment`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|transRefId|Id of the transaction details|4206d64d-b5e9-4edb-8d42-5568e827ab14|
|cryptoCurrencyType|Currency type of the payment
1 : BTC
2: ETH|2|

## getPowerballBanner

Powerball banner for displaying the games

### HTTP request

`GET {{URL}}/games/getPowerballBanner`

## profilePicUpdation

Updating the profile image of a user

### HTTP request

`POST {{URL}}/user/profilePicUpdation`

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|profilePicture|Profile picture of the user to be replaced||

## getWalletBalance

Get the balance in the wallet

### HTTP request

`GET {{URL}}/user/getWalletBalance`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## viewWinners

Display the winners of a game

### HTTP request

`GET {{URL}}/games/viewWinners`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## listCountry

List the entire country

### HTTP request

`GET {{URL}}/master/listCountry`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## User Login

Login section of the user

### HTTP request

`POST {{URL}}/user/login`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|username|username of the user|sijo@accubits.com|
|password|password of the user|Sijo@123|
|device|optional. only for mobile devices|mobile|

## powerball draftTickets

Drafting power ball tickets

### HTTP request

`POST {{URL}}/powerball/draftTickets`

> POST raw data JSON:

```json
{
   "contestId":"1",
   "amount":"6",
   "noOfTickets":2,
   "isPowerPlay":"true",
   "ticketNumbers":[
      {
         "whiteball1":"2",
         "whiteball2":"3",
         "whiteball3":"34",
         "whiteball4":"45",
         "whiteball5":"46",
         "powerball":"3"
      },
      {
         "whiteball1":"12",
         "whiteball2":"32",
         "whiteball3":"14",
         "whiteball4":"44",
         "whiteball5":"4",
         "powerball":"3"
      }
   ]
}
```

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/json|

## getDepositAddress

Get the deposit address of payment

### HTTP request

`POST {{URL}}/payment/getDepositAddress`

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|transRefId|Id of the transaction details|dac2ef1e-37d1-4423-820f-404457334af5|
|paymentCurrency|Currency type of the payment
1 : BTC
2: ETH|1|

## getStatus

Get the status of the transactions

### HTTP request

`POST {{URL}}/payment/getStatus`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|transRefId|Id of the transaction details|dac2ef1e-37d1-4423-820f-404457334af5|

## viewGames

Dispalying the details of the games

### HTTP request

`GET {{URL}}/games/viewGames`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## profileUpdation

Updating the details of a user

### HTTP request

`POST {{URL}}/user/profileUpdation`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||C4xUel_FJ|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|firstName|First name of the user (Maximun length 50 characters)|vigin|
|lastName|Last name of the user(Maximun length 50 characters)|vp|
|dob|Date of birth of the user|1995-04-04|
|phoneNo|Phone number of the user (Minimum length is 10 and maximum length is 20)|2ds|
|country|Country of the user(Drop down)|1|
|state|State of the user (Maximun length 50 characters)|jkgkj|
|city|City of the user (Maximun length 50 characters)|ujguog|
|zip|Zip code of the user(Maximun length 50 characters)|3|
|streetAddress|Street address of the user(Maximun length 100 characters)|hgdhtjdjtd|

## user logout

Logout the session

### HTTP request

`GET {{URL}}/user/logout`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## cancel payment

To cancel a ongoing payment

### HTTP request

`POST {{URL}}/payment/cancel`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|transRefId|Id of the transaction details|dac2ef1e-37d1-4423-820f-404457334af5|

## UserDetails

Getting the details of a specific user

### HTTP request

`GET {{URL}}/user/getUserDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||C4xUel_FJ|

## getResults

Get the results of a particular game

### HTTP request

`POST {{URL}}/games/getResults`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|page|Page number to be displayed|1|
|gameType|Type of the game (1 : powerball)|1|
|drawDate|optional ; Draw date of the result|2011-11-01|

## forgotPassword

API for forgot password

### HTTP request

`POST {{URL}}/user/forgotPassword`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|emailId|Email address to which the forgot password link has to be send|vigin@accubits.com|

## passwordReset

Resetting the user's password

### HTTP request

`POST {{URL}}/user/passwordReset`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||cv-WB4yQh|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|newPassword|New password of the user|sijo12345|
|confirmPassword|Confirm password of the user|sijo12345|

## getGameDetails

Get the details ofthe on going games

### HTTP request

`GET {{URL}}/user/getGameDetails?pageNumber=1&limit=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||C4xUel_FJ|

### Query Params

|Parameter|Description|Value|
|---|---|---|
|pageNumber|Page number to be displayed|1|
|limit|Limit of the details displayed in a  page|1|

## generateQRCode

Generate the QR code

### HTTP request

`GET {{URL}}/payment/generateQRCode?text=text&width=150`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|text|Text to be encoded in QR Code|text|
|width|optional Size of the QR Code to be displayed (Default :150px)|150|

## passwordUpdate

Updating the user password

### HTTP request

`POST {{URL}}/user/passwordUpdate`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||cv-WB4yQh|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|currentPassword|Current password of the user|sijo1234|
|newPassword|New password of the user|sijo12345|
|confirmPassword|Confirm the new password of the user|sijo12345|

## checkUserParticipation

Check whether the user is participated or not

### HTTP request

`GET {{URL}}/games/checkUserParticipation/1`

## viewResults

Display the results of the game

### HTTP request

`GET {{URL}}/games/viewResults`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getSummary

Get the summary of the transactions

### HTTP request

`POST {{URL}}/payment/getSummary`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|transRefId|Id of the transaction details|4206d64d-b5e9-4edb-8d42-5568e827ab14|
|paymentType|Payment method type
1 - wallet 
2 - using third party crypto
3 - fiat|1|

## pickRandomTickets

Generating random tickets for game

### HTTP request

`GET {{URL}}/powerball/pickRandomTickets/20`

## contactDetails

Contact the admin for an enquiry

### HTTP request

`POST {{URL}}/user/contactDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

### POST parameters

|Parameter|Description|Example|
|---|---|---|
|fullName|Full name of the enquirer|vigin|
|email|Email address of the enquirer|vigin@accubits.com|
|subject|Subject of the enquiry|Problem|
|message|Message details of the enquiry|qwertyuiwertyutrdsdfghjhgfdjkjdgfhjhfgkgsttruiuyrtyudfcvvcvbnvbm,mncvbnbvvtdhghuftgyertdfhcgvtygfcythgtyfgqwerqwertyuiwertynvbm,mncvbnbvvtdhghuftgyertdfhcgvtygfcythgtyfgqwertyuiwertyutrdsdfghjhgfdjkjdgfhjhfgkgsttruiuyrtyudfcvvcvbnvbm,mncvbnbvvtdhghuftgyertdfhcgvtygfcythgtyfgqwertyuiwertyutrdsdfghjhgfdjkjdgfhjhfgkgsttruiuyrtyudfcvvcvbnvbm,mncvbnbvvtdhghuftgyertdfhcgvtygfcythgtyfg|

## getProfilePic

Get the profile picture of user

### HTTP request

`GET {{URL}}/user/getProfilePic`

## getUSDvalue

Conversiopn of crypto currenct to USD

### HTTP request

`GET {{URL}}/payment/getUSDvalue?currency=BTC&amount=2`

### Query Params

|Parameter|Description|Value|
|---|---|---|
|currency|Currency to be select for getting corresponding USD value(BTC and ETH)|BTC|
|amount|Amount to be checked|2|

