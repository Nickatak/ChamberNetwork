Houston Chamber Network - initial project

Parts list:

- Public (app)
	- Functionalities necessary:
		- [ ] Register Musician
		- [ ] Register Coach

	- Views necessary:
		- [x] Welcome page (localhost/public/welcome/)
			- [x] Background images parallax
			- [x] Navbar top
				- [x] Link to welcome (active)
				- [x] Link to register_member 
				- [x] Link to register_coach
				- [x] Link to calendar
				- [x] Link to login
			- [x] Footer
				- [x] Link to about
				- [x] Contact info

		- [x] About (localhost/public/about/)
			- [ ] Display pertinent text
				- [ ] Links w/in text
			- [x] Background image
			- [x] Navbar top
				- [x] Link to welcome (active)
				- [x] Link to register_member 
				- [x] Link to register_coach
				- [x] Link to calendar
				- [x] Link to login
			- [x] Footer
				- [x] Link to about
				- [x] Contact info

		- [x] Register member page (localhost/public/register_member/)
			- [ ] Form
				- [ ] Field for first name
				- [ ] Field for last name
				- [ ] Field for email
				- [ ] Field for password
				- [ ] Drop-down menu for primary instrument
				- [ ] Drop-down menu for secondary instrument
				- [ ] Submit button
			- [ ] Validations for all fields
			- [ ] Render Login upon successful registration
			- [ ] Link to Register (active)
			- [ ] Link to Login

		- [x] Register coach page (localhost/public/register_coach/)
			- [ ] Form
				- [ ] Field for first name
				- [ ] Field for last name
				- [ ] Field for email
				- [ ] Field for password
				- [ ] Drop-down menu for primary instrument
				- [ ] Drop-down menu for secondary instrument
				- [ ] Submit button
			- [ ] Validations for all fields
			- [ ] Render Login upon successful registration
			- [ ] Link to Register (active)
			- [ ] Link to Login

- Musicians (app)
	- Functionalities necessary:
		- [ ] Login Musician
		- [ ] Logout Musician (must be possible on multiple pages)
		- [ ] Individual musician details
		- [ ] Dashboard 
			 [ ] Edit Musician information [TODO]

	- Information necessary:
		- Musician model
			- [ ] Musician first name (text)
			- [ ] Musician last name (text)
			- [ ] Musician email (text)
			- [ ] Musician password (text)
			- [ ] Musician primary instrument
			- [ ] Musician secondary instrument
			- [ ] Musician level [TODO]
			- [ ] Musician description [TODO]
			- [ ] Musician approved (Boolean)
			- [ ] Created at (datetime)
			- [ ] Updated at (datetime)

	- Views necessary:
		- [x] Login page (localhost/musicians/login/)
			- [ ] Login form 
				- [ ] Email field
				- [ ] Password field
				- [ ] Submit button
			- [ ] Render Musician Dashboard Page upon upon successful login
			- [ ] Link to Register
			- [ ] Link to Login (active)

		- [x] Logout Musician (not a page, just a view) (localhost/musicians/logout/)
			- [ ] Logout Musician and redirect to login page

		- [x] Individual Musician page (localhost/musicians/musician/[id]/)
			- [ ] Display musician information (card)
				- [ ] First name
				- [ ] Last name
				- [ ] Email
				- [ ] Primary instrument
				- [ ] Secondary instrument
				- [ ] Musician level
				- [ ] Musician description
				- [ ] Musician's performances (each performance a link to individual performance page)
			- [ ] Link to Home page 
			- [ ] Link to Add Performance page
			- [ ] Link to Instruments page
			- [ ] Link to Calendar page
			- [ ] Link to Logout 

		- [x] Musician Dashboard page (localhost/musicians/dashboard/)
			- [ ] Text that says "Welcome [Musician first name]!"
			- [ ] Display Musician information (card):
				- [ ] Last name
				- [ ] Email
				- [ ] Primary instrument
				- [ ] Secondary instrument
			- [ ] Upcoming performances (card):
				- [ ] Title of performance w/date : Each is a link to individual performance page
			- [ ] Collaborators (card) 
				- [ ] Each name provides a link to that Musicians's page
			- [ ] Link to Dashboard page (active)
			- [ ] Link to Add Performance page
			- [ ] Link to Instruments page
			- [ ] Link to Calendar page
			- [ ] Link to Logout

- Performances (app)
	- Functionalities necessary:
		- [ ] Add performances to db
		- [ ] View individual performance details
		- [ ] View all upcoming performances (Calendar) [TODO]

	- Information necessary:
		- Performance model:
			- [ ] Title (i.e. "Mozart Chamber Works")
			- [ ] Description of performance (further detail)
			- [ ] Date of performance
			- [ ] Time of performance
			- [ ] Location of performance
			- [ ] Musician(s) involved (M2M)
			- [ ] Created by (Musician) (FK)
			- [ ] Created at
			- [ ] Updated at

	- Views necessary:
		- [ ] Add performance page (localhost/performances/add)
			- [ ] Form to add performance:
				- [ ] Field for title
				- [ ] Field for description
				- [ ] Field for date
				- [ ] Field for time
				- [ ] Field for location
				- [ ] Validations: must complete form
				- [ ] Validation: inform user if performance has already been added to db
				- [ ] Submit button
			- [ ] Link to Home page
			- [ ] Link to Add Performance page (active)
			- [ ] Link to Instruments page
			- [ ] Link to Calendar page
			- [ ] Link to Logout

		- [ ] Individual performance page (localhost/performances/performance/[id]/)
			- [ ] Performance info (card)
				- [ ] Title 
				- [ ] Description
				- [ ] Musician who created entry
				- [ ] Musicians involved (appear after added via form)
			- [ ] Form to add additional musicians to performance
				- [ ] Musician first name
				- [ ] Musician last name
				- [ ] Musician instrument
				- [ ] Submit button
			- [ ] Link to Home page
			- [ ] Link to Add Performance page
			- [ ] Link to Instruments page
			- [ ] Link to Calendar page
			- [ ] Link to Logout

		- [ ] Calendar page (localhost/performances/calendar/) [TODO]
			- [ ] For now, just text that says "Under construction"
			- [ ] In calendar form, a list of all performances upcoming in network
				- [ ] Each performance title is a link to that performance's individual page
			- [ ] Link to Home page
			- [ ] Link to Add Performance page
			- [ ] Link to Instruments page
			- [ ] Link to Calendar page (active)
			- [ ] Link to Logout

- Instruments (app) 
	- [ ] Functionalities necessary:
		- [ ] Search for Musicians by instrument

	- Instrument model:
		- [ ] Instrument name
		- [ ] Musician (M2M)
		- [ ] Created at
		- [ ] Updated at

	- [ ] Views necessary:
		- [x] Individual instrument page (localhost/performances/instruments/[id]/) (static)
			- [ ] Text that says "Page for [instrument]"
			- [ ] List of all musicians in db who play instrument (only first, last names)
			- [ ] Each musician name is a link to that musician's individual page
			- [ ] Link to Home page
			- [ ] Link to Add Performance page
			- [ ] Link to Instruments page
			- [ ] Link to Calendar page
			- [ ] Link to Logout
		




