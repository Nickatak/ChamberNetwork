Houston Chamber Network - initial project

Parts list:

- Public (app)
	- Functionalities necessary:
		- [ ] Register Musician
		- [ ] Register Coach
		- [ ] Register Supporter

	- Views necessary:
		- [x] Welcome page (houstonchambermusic.org/public/welcome/)
			- [x] Background images parallax w/ text and links
			- [x] Navbar top
				- [x] Link to Welcome (active)
				- [x] Link to Register as Member
				- [x] Link to Register as Coach
				- [x] Link to Receive e-Newsletter
				- [x] Link to Login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [x] About (houstonchambermusic.org/public/about/)
			- [ ] Display pertinent text
				- [ ] Links w/in text
			- [x] Background image
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member
				- [x] Link to Register as CoachI have 
				- [ ] Link to Receive e-Newsletter
				- [x] Link to login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [x] Register Supporter Page (houstonchambermusic.org/public/register_supporter)
			- [ ] Form
				- [ ] First name
				- [ ] Last name
				- [ ] Email
				- [ ] Address
					- [ ] Street number
					- [ ] Unit
					- [ ] City
					- [ ] State
					- [ ] Zip
				- [ ] Phone
				- [ ] Submit button
			- [ ] Validations for all fields
			- [ ] Render success page upon successful submission
			- [ ] Navbar top
				- [ ] Link to Welcome 
				- [ ] Link to Register as Member
				- [ ] Link to Register as Coach
				- [ ] Link to Receive e-Newsletter (active)
				- [ ] Link to login
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [x] Register member page (houstonchambermusic.org/public/register_member/)
			- [ ] "What happens after you submit form" explanation
			- [x] Form
				- [x] First name
				- [x] Last name
				- [x] Email
				- [x] Address
					- [x] Street number
					- [x] Unit
					- [x] City
					- [x] State
					- [x] Zip
				- [x] Brief musical bio
				- [x] Drop-down menu for primary instrument
				- [x] Drop-down menu for secondary instrument
				- [x] Submit button
			- [ ] Validations for all fields
			- [ ] Send email to Michael upon successful submission
			- [ ] Render success page upon successful submission
			- [ ] Navbar top
				- [ ] Link to Welcome 
				- [ ] Link to Register as Member (active)
				- [ ] Link to Register as Coach
				- [ ] Link to Receive e-Newsletter
				- [ ] Link to Login
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info  

		- [x] Register coach page (houstonchambermusic.org/public/register_coach/)
			- [ ] Form
				- [ ] First name
				- [ ] Last name
				- [ ] Email
				- [ ] Address
					- [ ] Street number
					- [ ] Unit
					- [ ] City
					- [ ] State
					- [ ] Zip
				- [ ] Load CV
				- [ ] Brief musical bio
				- [ ] Drop-down menu for primary instrument
				- [ ] Drop-down menu for secondary instrument
				- [ ] Submit button
			- [ ] Validations for all fields
			- [ ] Send email to Michael upon successful submission
			- [ ] Render success page upon successul submission
			- [ ] Navbar top
				- [ ] Link to Welcome 
				- [ ] Link to Register as Member 
				- [ ] Link to Register as Coach (active)
				- [ ] Link to Receive e-Newsletter
				- [ ] Link to Login
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [ ] Success page (houstonchambermusic.org/public/success)
			- [ ] Success message(s) 
				- [ ] For member
				- [ ] For coach
				- [ ] For supporter
			- [ ] Navbar top
				- [ ] Link to Welcome 
				- [ ] Link to Register as Member 
				- [ ] Link to Register as Coach (active)
				- [ ] Link to Receive e-Newsletter
				- [ ] Link to Login
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [ ] Login page (houstonchambermusic.org/public/login/)
			- [ ] Login form
				- [ ] Field for email
				- [ ] Field for password
				- [ ] Validations
				- [ ] Submit button
			- [ ] Render member/coach dashboard page upon successful login
			- [ ] Navbar top
				- [ ] Link to Welcome 
				- [ ] Link to Register as Member 
				- [ ] Link to Register as Coach
				- [ ] Link to Receive e-Newsletter
				- [ ] Link to Login (active)
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

- Musicians (app)
	- Functionalities necessary:
		- [ ] Login member/coach
		- [ ] Logout member/coach (must be possible on multiple pages)
		- [ ] Edit member/coach information

	- Information necessary:
		- [ ] Musician model
			- [ ] First name (text)
			- [ ] Last name (text)
			- [ ] Email (text)
			- [ ] Password (text)
			- [ ] Primary instrument
			- [ ] Secondary instrument
			- [ ] Rating (1-5 or coach)
			- [ ] Brief bio 
			- [ ] Approval (Boolean)
			- [ ] Created at (datetime)
			- [ ] Updated at (datetime)

	- Views necessary:
		- [x] Musician Dashboard page (houstonchambermusic.org/musicians/dashboard/)
			- [ ] Text that says "Welcome [Musician first name]!"
			- [ ] Display Musician information (card):
				- [ ] Full name
				- [ ] Email
				- [ ] Primary instrument
				- [ ] Secondary instrument
				- [ ] Rating
				- [ ] Bio
				- [ ] Edit function
			- [ ] Upcoming performances (card):
				- [ ] Title of performance w/date : Each is a link to individual performance page
			- [ ] Navbar top
				- [ ] Link to Dashboard (active)
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [x] Individual Musician page (houstonchambermusic.org/musicians/musician/[id]/)
			- [ ] Display musician information (card)
				- [ ] First name
				- [ ] Last name
				- [ ] Email
				- [ ] Primary instrument
				- [ ] Secondary instrument
				- [ ] Rating
				- [ ] Bio
			- [ ] Upcoming performances (card):
				- [ ] Title of performance w/date : Each is a link to individual performance page
			- [ ] Navbar top
				- [ ] Link to Dashboard 
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [ ] Logout (not a page, just a view) (houstonchambermusic.org/musicians/logout/)
			- [ ] Logout Musician and redirect to login page 

- Performances (app)
	- Functionalities necessary:
		- [ ] Add performances to db
		- [ ] Edit performance in db
		- [ ] View individual performance details
		- [ ] View Upcoming performances: site must automatically add and subtract performances based on date
		- [ ] Generate email content on performances

	- Information necessary:
		- Performance model:
			- [ ] Title (i.e. "Mozart Chamber Works")
			- [ ] Description of performance (further detail)
			- [ ] Date of performance
			- [ ] Time of performance
			- [ ] Location of performance
			- [ ] Musician(s) involved (M2M)
				- [ ] First name
				- [ ] Last name
				- [ ] Instrument
			- [ ] Created by (Musician) (FK)
			- [ ] Created at
			- [ ] Updated at

	- Views necessary:
		- [ ] Add performance page (houstonchambermusic.org/performances/add)
			- [ ] Form to add performance:
				- [ ] Title
				- [ ] Description
				- [ ] Date
				- [ ] Time
				- [ ] Address
					- [ ] Street number
					- [ ] Unit
					- [ ] City
					- [ ] State
					- [ ] Zip
				- [ ] Validations: must complete
				- [ ] Validation: inform user if performance has already been added to db
				- [ ] Submit button
			- [ ] Navbar top
				- [ ] Link to Dashboard 
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance (active)
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [ ] Individual performance page (houstonchambermusic.org/performances/performance/[id]/)
			- [ ] Performance info (card)
				- [ ] Title 
				- [ ] Description
				- [ ] Location
				- [ ] Date
				- [ ] Time
				- [ ] Musician who created entry
				- [ ] Musicians involved (w/ links to their pages)
				- [ ] Edit information (only by member who created event)
			- [ ] Form to add additional musicians to performance
				- [ ] First name
				- [ ] Last name
				- [ ] Instrument
				- [ ] Submit button
			- [ ] Navbar top
				- [ ] Link to Dashboard 
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance 
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [ ] Upcoming performances page (houstonchambermusic.org/performances/upcoming/)
			- [ ] List of performances, by date
				- [ ] Title
				- [ ] Description
				- [ ] Date
				- [ ] Time
				- [ ] Location
			- [ ] Site must automatically add and subtract performances (by date)
			- [ ] Each performance provides link to Individual Performance page

- Instruments (app) 
	- [ ] Functionalities necessary:
		- [ ] Search for Musicians by instrument

	- Instrument model:
		- [ ] Instrument name
		- [ ] Musicians (M2M)
		- [ ] Created at
		- [ ] Updated at

	- [ ] Views necessary:
		- [x] Individual instrument page (houstonchambermusic.org/performances/instruments/[name]/) 
			- [ ] Text that says "Page for [instrument]"
			- [ ] List of all musicians in db who play instrument (first name, last name, rating)
			- [ ] Each musician name is a link to that musician's individual page
			- [ ] Navbar top
				- [ ] Link to Dashboard 
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance 
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		




