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

## userTicketResults

List the tickets taken for a game

### HTTP request

`GET {{URL}}/user/userTicketResults?pageNumber=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||C4xUel_FJ|

## getWinnerSummary

Get the winners summary

### HTTP request

`GET {{URL}}/games/getWinnerSummary/1`

### Headers

## userList

List the entire users in the platform

### HTTP request

`GET {{URL}}/admin/userList?pageNumber=1&limit=2&searchQuery`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getTransactionHistory

Get the transaction history of the user

### HTTP request

`POST {{URL}}/user/getTransactionHistory`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## userContestResults

Displaying the contests participants details

### HTTP request

`GET {{URL}}/admin/userContestResults?id=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## registration

Registeration page of the user

### HTTP request

`POST {{URL}}/user/registration`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getWalletHistory

Get the wallet history of the user

### HTTP request

`POST {{URL}}/user/getWalletHistory`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getUserWalletTransactions

Get all the wallet transactions of individual users

### HTTP request

`GET {{URL}}/admin/getUserWalletTransactions?page=1&limit=100&userId=4&date=2019-10-03&status=1`

### Headers

## makeWalletPayment

Make the payment for the game

### HTTP request

`POST {{URL}}/payment/makeWalletPayment`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getPowerballBanner

Powerball banner for displaying the games

### HTTP request

`GET {{URL}}/games/getPowerballBanner`

### Headers

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

## ongoingGamesList

Listing the ongoing games

### HTTP request

`GET {{URL}}/admin/ongoingGamesList`

### Headers

## profilePicUpdation

Updating the profile image of a user

### HTTP request

`POST {{URL}}/user/profilePicUpdation`

### Headers

## getEarningSummary

Get the summary of the earnings

### HTTP request

`GET {{URL}}/admin/getEarningSummary?year=2019`

### Headers

## deleteUser

Delete a user from the platform

### HTTP request

`POST {{URL}}/admin/deleteUser`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

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

## powerball draftTickets

Drafting power ball tickets

### HTTP request

`POST {{URL}}/powerball/draftTickets`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/json|

## getDepositAddress

Get the deposit address of payment

### HTTP request

`POST {{URL}}/payment/getDepositAddress`

### Headers

## usertransactionDetails

Get the transaction details of a user

### HTTP request

`GET {{URL}}/admin/usertransactionDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getStatus

Get the status of the transactions

### HTTP request

`POST {{URL}}/payment/getStatus`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## recentGames

Listing the recent games

### HTTP request

`GET {{URL}}/admin/recentGames`

### Headers

## removePowerballWinner

Changing the powerball winner

### HTTP request

`POST {{URL}}/admin/removePowerballWinner`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

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

## removeContest

Remone the details of a contest

### HTTP request

`DELETE {{URL}}/admin/removeContest/6`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

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

## Admin Login

Login for the admin

### HTTP request

`POST {{URL}}/admin/login`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

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

## powerballParticipantsDetails

Listing the details of a powerball participants

### HTTP request

`GET {{URL}}/admin/powerballParticipantsDetails?contestId=29&searchQuery=name&pageNumber=1&limit=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getPowerballDraftResult

Get the powerball game result

### HTTP request

`GET {{URL}}/admin/getPowerballDraftResult/1`

### Headers

## updatePowerballResult

Updating the powerball results

### HTTP request

`POST {{URL}}/admin/updatePowerballResult`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getWalletTransactions

Get all the wallet transactions

### HTTP request

`GET {{URL}}/admin/getWalletTransactions?page=1&limit=10&date=2019-10-04&type=1&status=`

### Headers

## updateContestDetails

Updating the details of the contest

### HTTP request

`POST {{URL}}/admin/updateContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## forgotPassword

API for forgot password

### HTTP request

`POST {{URL}}/user/forgotPassword`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getWalletOverview

Get the overview of the wallet

### HTTP request

`GET {{URL}}/admin/getWalletOverview`

### Headers

## getTransactions

Get all the transaction details

### HTTP request

`GET {{URL}}/admin/getTransactions?page=1&limit=100&date=2019-10-04&status=5`

### Headers

## passwordReset

Resetting the user's password

### HTTP request

`POST {{URL}}/user/passwordReset`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||cv-WB4yQh|

## getWalletBalance

Get the wallet balance of admin

### HTTP request

`GET {{URL}}/admin/getWalletBalance?userId=1`

### Headers

## getAllContestDetails

Get all the contest details

### HTTP request

`POST {{URL}}/admin/getAllContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getContestDetails

Get the details of a contest

### HTTP request

`POST {{URL}}/admin/getContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## publishPowerballResult

Publish the powerball result

### HTTP request

`POST {{URL}}/admin/publishPowerballResult`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## viewUser

Display the details of a particular user

### HTTP request

`GET {{URL}}/admin/viewUser?id=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getGameDetails

Get the details ofthe on going games

### HTTP request

`GET {{URL}}/user/getGameDetails?pageNumber=1&limit=1`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||C4xUel_FJ|

## generateQRCode

Generate the QR code

### HTTP request

`GET {{URL}}/payment/generateQRCode?text=text&width=150`

### Headers

## passwordUpdate

Updating the user password

### HTTP request

`POST {{URL}}/user/passwordUpdate`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|
|Authorization||cv-WB4yQh|

## checkUserParticipation

Check whether the user is participated or not

### HTTP request

`GET {{URL}}/games/checkUserParticipation/1`

### Headers

## viewResults

Display the results of the game

### HTTP request

`GET {{URL}}/games/viewResults`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## blockUser

Blocking a user from platform

### HTTP request

`POST {{URL}}/admin/blockUser`

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

## getParticipantsDetailsToCsv

Get all the participants of a contest in csv format

### HTTP request

`GET {{URL}}/admin/getParticipantsDetailsToCsv?contestId=103`

### Headers

## pickRandomTickets

Generating random tickets for game

### HTTP request

`GET {{URL}}/powerball/pickRandomTickets/20`

### Headers

## getUserTransactions

Get all the user transactions

### HTTP request

`GET {{URL}}/admin/getUserTransactions?page=1&limit=10&userId=4`

### Headers

## userUnBlock

Unblock a blocked user

### HTTP request

`POST {{URL}}/admin/userUnBlock`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## contactDetails

Contact the admin for an enquiry

### HTTP request

`POST {{URL}}/user/contactDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## setContestDetails

Setting the contest details of the game

### HTTP request

`POST {{URL}}/admin/setContestDetails`

### Headers

|Parameter|Description|Value|
|---|---|---|
|Content-Type||application/x-www-form-urlencoded|

## getPaymentOverview

Get the overview of the payments

### HTTP request

`GET {{URL}}/admin/getPaymentOverview`

### Headers

## getProfilePic

Get the profile picture of user

### HTTP request

`GET {{URL}}/user/getProfilePic`

### Headers

## getUSDvalue

Conversiopn of crypto currenct to USD

### HTTP request

`GET {{URL}}/payment/getUSDvalue?currency=BTC&amount=2`

### Headers


