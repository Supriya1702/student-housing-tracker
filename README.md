Student Housing Tracker
Overview
The Student Housing Tracker is a web-based platform designed to simplify the process of finding on-campus and off-campus housing for students at the University of Massachusetts Amherst. Addressing the challenges of scattered information and the ongoing housing crisis, this platform provides a centralized hub for students to search, filter, and interact with rental listings. It enables landlords to post properties and facilitates secure communication, reviews, and verifications to ensure a trustworthy and efficient housing search experience.

Project Links

GitHub Repository: github.com/Supriya1702/student-housing-tracker
Google Drive Documentation: [Google Drive Folder](https://drive.google.com/drive/folders/1Wqjl_v2kOTAjIWhgIsaOM78_e0i1hLZR?usp=drive_link)
Final Video Demonstration:  https://drive.google.com/file/d/1snTuJwaw0EWNLtr3hbfboedpe3H1t818/view?usp=drive_link

Features

Listings: Students and landlords can post and view detailed rental listings, including price, location, amenities, and availability.
Search & Filter: Filter listings by price, distance from campus, room type, pet-friendliness, and amenities for personalized results.
Map Integration: Visualize listing locations on an interactive map with Google Maps API, showing proximity to campus and amenities.
Reviews & Ratings: Verified tenants can leave reviews and ratings for properties, with moderation for authenticity.
Secure Messaging: Students and landlords can communicate securely to discuss listings or schedule tours.
Saved Listings: Students can save favorite listings for easy access and receive notifications if listings become unavailable.
User Verification: Users submit documents (e.g., ID, lease) to build trust, with admin-managed verification processes.

Tech Stack

Frontend: React.js with Vite and Tailwind CSS for a responsive, component-based UI.
Backend: Django (Python) with RESTful APIs for secure and scalable request handling.
Database: PostgreSQL with PostGIS for structured data and geospatial queries.
Authentication: JWT (JSON Web Tokens) for role-based access control (Student, Landlord, Admin).
Storage: AWS S3 for hosting property images and user documents.
APIs: Google Maps API for location services; Elasticsearch for real-time search.
Additional Tools: BeautifulSoup for data scraping, Requests for API calls, Redis for caching.

Installation and Setup
Prerequisites

Python 3.9+
Node.js 16+
PostgreSQL 14+ with PostGIS extension/MySql
AWS account (for S3 and deployment)
Docker (optional, for containerized deployment)

Steps

Clone the Repository:
git clone https://github.com/Supriya1702/student-housing-tracker.git
cd student-housing-tracker


Backend Setup:

Navigate to the backend directory:cd backend


Install dependencies:pip install -r requirements.txt


Configure environment variables in .env:DATABASE_URL=ABCD
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
GOOGLE_MAPS_API_KEY=your_key


Run migrations:python manage.py migrate


Start the Django server:python manage.py runserver




Frontend Setup:

Navigate to the frontend directory:cd ../frontend


Install dependencies:npm install


Start the development server:npm run dev



Update the database URL in the backend .env file.


Run the Application:

Access the frontend at http://localhost:3000 and the backend API at http://localhost:8000.



Data Model
The database consists of six tables:

users_user: Stores user details (user_id, email, role: Student/Landlord/Admin).
listings_listing: Stores rental listings (listing_id, price, location, amenities).
listings_review: Stores user reviews (review_id, rating, comment).
listings_savedlisting: Stores favorited listings (saved_id).
listings_message: Stores user messages (message_id, content).
users_verification: Stores verification documents (verification_id, status).

Relationships

User to Review (1:N)
Listing to Review (1:N)
User to SavedListing (1:N)
Listing to SavedListing (1:N)
User to Message (Sender/Receiver, 1:N)
Listing to Message (0:1 to N, optional)
User to Verification (1:N)

Challenges & Risks

Listing Accuracy: Risk of outdated or fraudulent listings requires constant verification.
Security: Secure messaging and document uploads need robust encryption.
Scalability: High user traffic during semester starts may cause performance issues.
Legal Compliance: Ensuring listings comply with subletting regulations.

Mitigations

Implement automated listing verification and spam detection.
Use end-to-end encryption and RBAC for secure data handling.
Optimize database queries with indexing and caching (Redis).
Consult legal guidelines for housing policies.

Evaluation

Functional Testing: Verified user authentication, listing creation, search, map view, messaging, and saved listings via unit and integration tests.
Usability: Peer testing (5 classmates) yielded a 4.4/5 average score, praising intuitive navigation but suggesting loading indicators.
Security: Implemented RBAC, JWT authentication, and admin-only access to verification data.
Performance: Optimized for 100 concurrent users with <2s search response times.

Lessons Learned

API Planning: Early API endpoint design prevented frontend-backend mismatches.
Team Collaboration: Weekly check-ins and GitHub issue tracking kept the team aligned.
Tech Stack: React’s Virtual DOM and Django’s ORM simplified development, but integration required careful debugging.

Future Plans

Add real-time chat and notifications.
Implement email verification and two-factor authentication.
Enhance scalability with sharding and load balancing.
Improve UI with hover effects and loading indicators.
Strengthen privacy with end-to-end encryption for messages and documents.

Contributing
We welcome contributions! Please follow these steps:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.


