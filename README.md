Houston Chamber Network - initial project

Parts list:

- Public (app)
    # Public itself won't have functionality, as its point is to simply house public route-URL's.

    - Breakdown of responsibilities:
    	- GB:
    		- Responsible for appearance of all pages (html and css)
    		- Responsible to rendering all pages (setting up urls and views to render pages) (will wait until NT has 		sketched in URL)
    		- Responsible for navigating within site (intra-site links)
    	- NT:
    		- Responsible for all back-end functions and comm with database

	- Views necessary:
		- [x] Welcome page (houstonchambermusic.org)
			- [x] URL path and view to render
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

		- [x] About (houstonchambermusic.org/about/)
			- [x] URL path and view to render
			- [ ] Display pertinent text
				- [ ] Links w/in text
			- [x] Background image
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member
				- [x] Link to Register as Coach
				- [x] Link to Receive e-Newsletter
				- [x] Link to login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [x] Register Patron Page (houstonchambermusic.org/new_patron)
			- [x] URL path and view to render
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
				- [x] Phone
				- [ ] Referred by
				- [x] Submit button
			- [ ] Validations for all fields
			- [ ] Render success page upon successful submission
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member
				- [x] Link to Register as Coach
				- [x] Link to Receive e-Newsletter (active)
				- [x] Link to login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [x] Register member page (houstonchambermusic.org/register_member/)
			- [x] URL path and view to render
			- [ ] Overlay: text for "What happens after I submit form"
			- [ ] Overlay: text for "ratings rubric"
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
				- [x] Phone number
				- [x] Brief musical bio
				- [x] Drop-down menu for primary instrument
				- [x] Drop-down menu for secondary instrument
				- [x] Self rating
				- [x] Submit button
			- [ ] Validations for all fields
			- [ ] Send email to Michael upon successful submission
			- [ ] Render success page upon successful submission
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member (active)
				- [x] Link to Register as Coach
				- [x] Link to Receive e-Newsletter
				- [x] Link to Login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info  

		- [x] Register coach page (houstonchambermusic.org/register_coach/)
			- [x] URL path and view to render
			- [ ] Overlay: test for "What happens after I submit this form?
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
				- [x] Phone number
				- [ ] Attach CV
				- [x] Brief musical bio
				- [x] Drop-down menu for primary instrument
				- [x] Drop-down menu for secondary instrument
				- [x] Submit button
			- [ ] Validations for all fields
			- [ ] Send email to Michael upon successful submission
			- [ ] Render success page upon successul submission
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member 
				- [x] Link to Register as Coach (active)
				- [x] Link to Receive e-Newsletter
				- [x] Link to Login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [x] Success page (houstonchambermusic.org/success/)
			- [ ] URL path and view to render
			- [x] Success message
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member 
				- [x] Link to Register as Coach (active)
				- [x] Link to Receive e-Newsletter
				- [x] Link to Login
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [x] Login page (houstonchambermusic.org/login/)
			- [ ] URL path and view to render
			- [x] Login form
				- [x] Field for email
				- [x] Field for password (encrypted)
				- [x] Validations
				- [x] Submit button
			- [x] Render member/coach dashboard page upon successful login
			- [x] Navbar top
				- [x] Link to Welcome 
				- [x] Link to Register as Member 
				- [x] Link to Register as Coach
				- [x] Link to Receive e-Newsletter
				- [x] Link to Login (active)
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info


- Users (app) #Former name: Musicians; both "members" and "coaches" are now simply "users." "Patrons" are not actually users of the site (have to login capabilities)

	- Breakdown of responsibilities:
    	- GB:
    		- Responsible for appearance of all pages (html and css)
    		- Responsible to rendering all pages (setting up urls and views to render pages) (will wait until NT has 		sketched in URL)
    		- Responsible for navigating within site (intra-site links)
    	- NT:
    		- Responsible for setting up database models
    		- Responsible for all back-end functions and comm with database

    # This is where the functionalities for public will tie to.
	- Functionalities necessary:
        - [ ] Register Musician
		- [ ] Register Coach
		- [ ] Register Patron
		- [ ] Login member/coach (aka user)
		- [ ] Logout member/coach (aka user) (must be possible on multiple pages)
		- [ ] Edit member/coach (aka user) information

	- Information necessary:
        - [x] Patron model
            - [x] First name 
            - [x] Last name 
            - [x] Email
            - [x] Street address
            - [x] Unit number
            - [x] City
            - [x] State 
            - [x] Zip
            - [x] Phone number
            - [x] Referred by (FK)
            - [x] Created at (datetime)
            - [x] Updated at (datetime)

        - [x] Musician model
            - [x] First name 
            - [x] Last name 
            - [x] Email 
            - [x] Password (encrypted)
            - [x] Street address
            - [x] Unit number
            - [x] City
            - [x] State
            - [x] Zip
            - [x] Phone number
            - [x] Primary instrument
            - [x] Secondary instrument
            - [x] Rating (1-5 or coach) (editable only by admin)
            - [x] Bio 
            - [x] Approval (Boolean)
            - [x] Created at (datetime)
            - [x] Updated at (datetime)		

	- Views necessary:
		- [x] User Dashboard page (houstonchambermusic.org/users/dashboard/)
			- Data needed
				- From User model:
					- [x] First name
					- [x] Last name
					- [x] Email
					- [x] Phone number
					- [x] Primary instrument
					- [x] Second instrument
					- [x] Rating
					- [x] Bio
				- From Performance model:
					- [ ] Title
					- [ ] Date
					- [ ] If under has no performances, message that says "You currently have no upcoming performances"
			- [x] URL path and view to render
			- [x] Display Musician information (card):
				- [x] Full name
				- [x] Email
				- [x] Phone number
				- [x] Primary instrument
				- [x] Second instrument
				- [x] Rating
				- [x] Bio
				- [ ] Edit function
			- [x] Upcoming performances (card):
				- [ ] Title of performance w/date : Each is a link to individual performance page
				- [x] For Beta: "Add performances feature is coming soon."
			- [x] Navbar top
				- [x] Link to Dashboard (active)
				- [x] Link to Upcoming Performances
				- [x] Link to Add Performance
				- [x] Drop-down menu for Instruments
					- [ ] Populated with instrument names
					- [ ] Each name a link to page
				- [ ] Logout
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

		- [ ] Individual member page #I am not sure about this URL: (houstonchambermusic.org/users/[id]/)
			- Data needed
				- From User model:
					- [ ] First name
					- [ ] Last name
					- [ ] Email
					- [ ] Phone number
					- [ ] Primary instrument
					- [ ] Second instrument
					- [ ] Rating
					- [ ] Bio
				- From Performance model:
					- [ ] Title
					- [ ] Date
					- [ ] If under has no performances, message that says "You currently have no upcoming performances"
			- [ ] URL path and view to render
			- [ ] Display musician information (card)
				- [ ] First name
				- [ ] Last name
				- [ ] Email
				- [ ] Phone number
				- [ ] Primary instrument
				- [ ] Secondary instrument
				- [ ] Rating
				- [ ] Bio
			- [ ] Upcoming performances (card):
				- [ ] Title of performance w/date : Each is a link to individual performance page
			- [ ] Message musician (send email)
			- [ ] Navbar top
				- [ ] Link to Dashboard 
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [ ] Edit member page #I am not sure about this URL: (houstonchambermusic.org/users/edit/[id]/)
			# I need to flesh this out!

		- [ ] Logout (not a page, just a view) (houstonchambermusic.org/users/logout/)
			- [ ] Logout Musician and redirect to login page 

- Performances (app) 
	# Note: performance app will not be completed (or perhaps even started) by beta launch date

	- Breakdown of responsibilities:
    	- GB:
    		- Responsible for appearance of all pages (html and css)
    		- Responsible to rendering all pages (setting up urls and views to render pages) (will wait until NT has 		sketched in URL)
    		- Responsible for navigating within site (intra-site links)
    	- NT:
    		- Responsible for setting up database models
    		- Responsible for all back-end functions and comm with database

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
		- [x] Add performance page (houstonchambermusic.org/performances/add/)
			- [x] For Beta : "Coming soon" message
			- [ ] URL path and view to render
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
				- [x] Link to Dashboard 
				- [x] Link to Upcoming Performances
				- [x] Link to Add Performance (active)
				- [x] Drop-down menu for Instruments
					- [ ] Populated with instrument names
					- [ ] Each name a link to page
				- [ ] Logout
			- [x] Footer
				- [x] Link to About Us
				- [ ] Contact info

		- [x] Individual performance page #I am not sure of this url: (houstonchambermusic.org/performances/[id]/)
			- [ ] URL path and view to render
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
			- [ ] Button to send rsvp for performance
			- [ ] Navbar top
				- [ ] Link to Dashboard 
				- [ ] Link to Upcoming Performances
				- [ ] Link to Add Performance 
				- [ ] Drop-down menu for Instruments
				- [ ] Logout
			- [ ] Footer
				- [ ] Link to About Us
				- [ ] Contact info

		- [x] Upcoming performances page (houstonchambermusic.org/performances/upcoming/)
			- [x] For Beta: "Coming soon" message
			- [ ] URL path and view to render
			- [ ] List of performances, by date
				- [ ] Title
				- [ ] Description
				- [ ] Date
				- [ ] Time
				- [ ] Location
			- [ ] Site must automatically add and subtract performances (by date)
			- [ ] Each performance provides link to Individual Performance page
			- [x] Navbar top
				- [x] Link to Dashboard 
				- [x] Link to Upcoming Performances (active)
				- [x] Link to Add Performance 
				- [x] Drop-down menu for Instruments
					- [ ] Populated with instrument names
					- [ ] Each name a link to page
				- [ ] Logout
			- [x] Footer
				- [x] Link to About Us
				- [x] Contact info

- Instruments (app) 

	- Breakdown of responsibilities:
    	- GB:
    		- Responsible for appearance of all pages (html and css)
    		- Responsible to rendering all pages (setting up urls and views to render pages) (will wait until NT has 		sketched in URL)
    		- Responsible for navigating within site (intra-site links)
    		- Provide list of instruments to be included in db (and therefore pull-down menus)
    	- NT:
    		- Responsible for setting up database models
    		- Responsible for all back-end functions and comm with database

	- [ ] Functionalities necessary:
		- [ ] Search for Musicians by instrument

	- Instrument model:
		- [ ] Instrument name
		- [ ] Musicians (M2M)
		- [ ] Created at
		- [ ] Updated at

	- [ ] Views necessary:
		- [ ] Individual instrument page (houstonchambermusic.org/instruments/[name]/) 
		- Data needed:
			- From Users model:
				- [ ] First name
				- [ ] Last name
				- [ ] Rating
				- [ ] Primary instrument
				- [ ] Second instrument
			- From Instruments model
				- [ ] Name of instrument
				- [ ] Connect names above ^ with each instrument
			- [ ] URL path and view to render
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

- Functionalities necessary for beta launch (1/14/19):
	Users (members and coaches) can submit registration form --> this initiates email to Michael, who works with new users (away from site) in order to approve them --> approved user is assigned a password and given go ahead to sign in --> user can sign in and see dashboard page --> user can edit personal information, including password

	Patrons will be able to sign up for e-newsletter. For now, this will just be sent to Michael, who can interact manually with patron as he sees fit. Later, much of this will need to be automated.

	In addition to dashboard page, individual member/coach page works also (recall that individual member/coach page is very similar to dashboard page - the same basic information is presented, but there are no edit capabilities)

	Instrument pull down menu works --> when user goes to individual instrument page, can see each user associated with instrument, then click on names to see their individual page.

	Some other pages (for example add_performance.html) will simply say "Coming Soon."

	Michael will need to be shown how to interact with admin page.

	Michelle will need to have time to deply site.

		




