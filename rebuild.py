import re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Meta and title
content = content.replace('[Your name here]', 'Aditi Sabne')
content = content.replace('[username], [name], skill', 'aditisabne, Aditi Sabne, Software Engineer, AI, ML, Flutter, C++')
content = content.replace('Hi, my name is <span class="text-color-main">Your Name</span>', 'Hi, my name is <span class="text-color-main">Aditi Sabne</span>')
content = content.replace("I'm the Unknown Developer.", "I'm a Result Driven Software Engineer.")
content = content.replace('src="assets/profile.jpg"', 'src="assets/aditi.jpeg"')
content = content.replace('This is where you can describe about yourself. The more you\n                describe about yourself, the more chances you have!', 'Result Driven Software Engineer with a strong background in Software Development, AI/ML and Database Management. Delivered 3+ end-to-end projects using Python, Java, MySQL, Flutter, Firebase, and OpenCV with hands-on experience in REST APIs, database-driven applications, and computer vision systems.')
content = content.replace('Extra Information about you! like hobbies and your goals.', 'Built practical solutions involving Real-time Features, Data-driven Decision-making, and Spearheaded development of SECURA women’s safety app integrating native Android SMS alerts via MethodChannel, cutting emergency response latency by 20%. Demonstrated technical capabilities through a National-Level Smart Cops Hackathon 2025 Win, competing against 1,322 registered participants.')

# Project 0
content = content.replace('<h3 class="project-wrapper__text-title">Project Title 0</h3>', '<h3 class="project-wrapper__text-title">SECURA — Women\'s Safety Companion App</h3>')
content = content.replace('''Describe the project being very specific, you can use the Twitter standard: no more than 280 characters: 
                    complement the information: the skills learned or reinforced in its realization and how you faced it, 
                    prove to be proactive in the search for solutions.''', '''<strong>Tech Stack:</strong> Flutter, Dart, Firebase, Gemini API<br>
                    Forged native Android integration via MethodChannel, enabling critical SMS alerts and improving user safety response times by 20%. Integrated Firebase Authentication and Firestore, enabling seamless user management and real-time data operations. Won 1st place at Smart Cops Hackathon 2025.''')

# Project 1
content = content.replace('<h3 class="project-wrapper__text-title">Project Title 1</h3>', '<h3 class="project-wrapper__text-title">SQL Query Engine & DBMS</h3>')
content = content.replace('''Demonstrate in this description the skills of a programmer: such as having commitment, 
                    having perseverance and accepting alternative solutions. Remember that being a portfolio you are not selling the project, 
                    you are selling yourself, it reflects the resources used: Frameworks, libraries, platforms, etc.''', '''<strong>Tech Stack:</strong> C++, DBMS, DSA, Data Structures, Algorithms<br>
                    Developed a custom SQL query engine in C++, implementing query parsing and execution for core operations including SELECT, INSERT, UPDATE, and DELETE. Implemented B+ Tree and hash-based indexing to optimize data retrieval, engineering core DBMS components to build a functional database engine.''')

# Project 2
content = content.replace('<h3 class="project-wrapper__text-title">Project Title 2</h3>', '<h3 class="project-wrapper__text-title">PresentX – Student & Teacher Connector</h3>')
content = content.replace('''If the project was collaborative, reflect it in this description, that will demonstrate communication and/or leadership skills. 
                    Additionally, if you made use of the mastery of a second language, it will reflect on you professionalism.''', '''<strong>Tech Stack:</strong> Flutter, Firebase, Supabase<br>
                    Developed a cloud-based academic management platform supporting attendance, assignments, role-based authentication, and real-time synchronization. Implemented secure backend services using Firebase, Supabase, REST APIs, and cloud database technologies.''')

# Contact
contact_form = '''
          <div class="contact-wrapper__text">
            <form action="#" class="contact__form">
              <div class="contact__form-field">
                <label class="contact__form-label" for="name">Name</label>
                <input
                  required
                  placeholder="Enter Your Name"
                  type="text"
                  class="contact__form-input"
                  name="name"
                  id="name"
                />
              </div>
              <div class="contact__form-field">
                <label class="contact__form-label" for="email">Email</label>
                <input
                  required
                  placeholder="Enter Your Email"
                  type="text"
                  class="contact__form-input"
                  name="email"
                  id="email"
                />
              </div>
              <div class="contact__form-field">
                <label class="contact__form-label" for="message">Message</label>
                <textarea
                  required
                  cols="30"
                  rows="10"
                  class="contact__form-input"
                  placeholder="Enter Your Message"
                  name="message"
                  id="message"
                ></textarea>
              </div>
              <button type="submit" class="btn btn--theme contact__btn">
                Submit
              </button>
            </form>
          </div>
'''
content = content.replace('<p class="contact-wrapper__text">[Put your call to action here]</p>', contact_form)
content = content.replace('mailto:example@email.com', 'mailto:aditirajusabne4@gmail.com')
content = content.replace('>Call to Action<', '>aditirajusabne4@gmail.com<')

# Update Demo Links properly
links = [
    'https://secura-women-safety.vercel.app/#/login',
    'https://lnkd.in/gP5N_Fy5',
    'https://present-xx.vercel.app/'
]

# We want to replace href="#!" ONLY if it's the See Live button.
# There are 3 blocks like this:
# <a rel="noreferrer" target="_blank" class="cta-btn cta-btn--hero" href="#!">See Live</a>
# We can use regex sub
for i, link in enumerate(links):
    content = re.sub(r'href="#!"(\s*>\s*See Live)', f'href="{link}"\\1', content, count=1)

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
