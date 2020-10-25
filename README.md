## Customstyle

for erpnext custom styles
installing App to ERPNext

`bench get-app customstyle https://github.com/michaeleino/erpnext-customstyle.git`

`bench install-app customstyle`

## To update this app ONLY
use bench exlude-app for all apps that needed not to be updated for ex:

   `bench exclude-app erpnext`
   
   `bench exclude-app frappe`

then run 

`bench update`

#### License

MIT
