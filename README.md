Student Housing Tracker 🏠
Welcome to the Student Housing Tracker, a sleek and intuitive web platform crafted to streamline the housing search for University of Massachusetts Amherst students. Tackling the challenges of fragmented information and the local housing crisis, our platform offers a centralized hub where students can effortlessly browse, filter, and engage with rental listings, while landlords can showcase their properties. With features like secure messaging, verified reviews, and interactive maps, we ensure a seamless and trustworthy experience for all users.
Team 7 - Student Housing TrackerCS 520: Software Engineering, Spring 2025University of Massachusetts Amherst

🌟 Project Overview
The Student Housing Tracker empowers students to navigate the complexities of finding on-campus and off-campus housing. By providing a user-friendly interface and robust features, we aim to reduce the stress of housing searches and foster trust through verified user interactions. Landlords benefit from easy listing management, while students enjoy personalized search options and secure communication channels.
Team


Resources

GitHub Repository: github.com/Supriya1702/student-housing-tracker\
Documentation: [Google Drive Folder](https://drive.google.com/drive/folders/1Wqjl_v2kOTAjIWhgIsaOM78_e0i1hLZR?usp=drive_link)\
Video Demo: https://drive.google.com/file/d/1snTuJwaw0EWNLtr3hbfboedpe3H1t818/view?usp=drive_link



✨ Key Features

Rental Listings: Create and explore detailed listings with pricing, location, amenities, and availability.
Smart Search & Filters: Narrow down options by price, campus proximity, room type, pet policies, or amenities.
Interactive Map: View listings on a Google Maps-powered interface, highlighting distances to campus and local amenities.
Reviews & Ratings: Verified tenants can share authentic feedback, moderated for reliability.
Secure Messaging: Connect directly with landlords to inquire about listings or arrange tours.
Saved Listings: Bookmark favorite properties and get notified if they become unavailable.
User Verification: Submit ID or lease documents for trust, managed by admin oversight.


🛠 Tech Stack
Our platform leverages modern technologies for performance, scalability, and user experience:

Frontend: React.js (with Vite) + Tailwind CSS for a dynamic, responsive UI.
Backend: Django (Python) with RESTful APIs for secure, scalable operations.
Database: PostgreSQL + PostGIS for robust data storage and geospatial queries.
Authentication: JWT for role-based access (Student, Landlord, Admin).
Storage: AWS S3 for secure image and document hosting.
APIs: Google Maps API for mapping; Elasticsearch for real-time search.
Tools: BeautifulSoup (data scraping), Requests (API calls), Redis (caching).
Deployment: AWS (EC2, RDS) with Docker and Kubernetes for scalability.


🚀 Getting Started
Prerequisites

Python 3.9+
Node.js 16+
PostgreSQL 14+ with PostGIS extension
AWS account (for S3 storage)
Docker (optional, for containerized deployment)

Installation Steps

Clone the Repository:
git clone https://github.com/Supriya1702/student-housing-tracker.git
cd student-housing-tracker


Set Up the Backend:

Navigate to the backend:cd backend


Install dependencies:pip install -r requirements.txt


Create a .env file with:DATABASE_URL= example_database
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
GOOGLE_MAPS_API_KEY=your_key


Apply migrations:python manage.py migrate


Launch the server:python manage.py runserver




Set Up the Frontend:

Navigate to the frontend:cd ../frontend


Install dependencies:npm install


Start the development server:npm run dev


Run the Application:

Frontend: http://localhost:3000
Backend API: http://localhost:8000



🗄 Data Model
The platform’s database comprises six core tables:

users_user: User profiles (user_id, email, role: Student/Landlord/Admin).
listings_listing: Rental properties (listing_id, price, location, amenities).
listings_review: User feedback (review_id, rating, comment).
listings_savedlisting: Favorited listings (saved_id).
listings_message: User communications (message_id, content).
users_verification: Verification documents (verification_id, status).

Relationships

User → Review (1:N): One user can write multiple reviews.
Listing → Review (1:N): One listing can have multiple reviews.
User → SavedListing (1:N): One user can save multiple listings.
Listing → SavedListing (1:N): One listing can be saved by multiple users.
User → Message (Sender/Receiver) (1:N): One user can send/receive multiple messages.
Listing → Message (0:1 to N): Messages may optionally reference a listing.
User → Verification (1:N): One user can submit multiple verification documents.


⚠️ Challenges & Mitigations
Challenges

Listing Accuracy: Outdated or fraudulent listings pose risks.
Security: Protecting user data in messaging and document uploads.
Scalability: Handling traffic spikes at semester starts.
Legal Compliance: Adhering to subletting regulations.

Mitigations

Automated verification and spam detection for listings.
End-to-end encryption and role-based access control (RBAC).
Database optimization with indexing and Redis caching.
Legal consultation to ensure compliance with housing policies.


📚 Lessons Learned

API Design: Early endpoint planning minimized integration issues.
Collaboration: Weekly syncs and GitHub streamlined teamwork.
Tech Stack: React’s Virtual DOM and Django’s ORM accelerated development, though debugging required precision.


🔮 Future Enhancements

Introduce real-time chat and push notifications.
Add email verification and two-factor authentication.
Scale with database sharding and load balancing.
Enhance UI with interactive hover effects and loading states.
Implement end-to-end encryption for messages and documents.


🤝 Contributing
We’d love your contributions! Follow these steps:

Fork the repository.
Create a feature branch: git checkout -b feature/your-feature
Commit changes: git commit -m "Add your feature"
Push to the branch: git push origin feature/your-feature
Submit a pull request.


