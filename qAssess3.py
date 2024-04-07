import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, text, answers, format_type="default"):
        self.text = text
        self.answers = answers
        self.format_type = format_type

    def display(self):
        if self.format_type == "default":
            print("Question: ", self.text)
        elif self.format_type == "formatted":
            print("Question:")
            print("---------------")
            print(self.text)
            print("---------------")
        else:
            print("Unsupported format type.")

        for answer in self.answers:
            print(answer)

class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Bowl")
        
        self.questions = {
            "Accounting": [],
            "Marketing": [],
            "Statistics": [],
            "Business Applications": []
        }

        self.answers = {
            "Accounting": [],
            "Marketing": [],
            "Statistics": [],
            "Business Applications": []
        }

        self.populate_questions_answers()

        self.create_category_selection()
    def populate_questions_answers(self):
        #Populate questions and answers for each category
        #Populate for Accounting
        self.questions["Accounting"] = [
            Question("Question 1: What is a balance sheet used for?", ["A. To track customer transactions", "B. To show the financial position of a company", "C. To manage inventory", "D. To calculate revenue"], "default"),
            Question("Question 2: What is the formula for calculating net income?", ["A. Assets = Liabilities + Equity", "B. Assets + Liabilities = Equity", "C. Assets - Liabilities = Equity", "D. Assets x Liabilities = Equity"], "default"),
            Question("Question 3: What is depreciation?", ["A. The amount of revenue earned", "B. The cost of goods sold", "C. The allocation of the cost of a tangible asset over its useful life", "D. The amount of dividends paid"], "default"),
            Question("Question 4: What is the purpose of a trial balance?", ["A. To track customer transactions", "B. To calculate net income", "C. To ensure that debits equal credits in the accounting records", "D. To manage inventory"], "default"),
            Question("Question 5: What is the difference between accounts payable and accounts receivable?", ["A. Accounts payable represents money owed by the company, while accounts receivable represents money owed to the company", "C. Accounts payable represents money owed to the company, while accounts receivable represents money owed by the company", "D. Accounts payable represents money invested in the company, while accounts receivable represents revenue earned by the company", "E. Accounts payable represents revenue earned by the company, while accounts receivable represents money invested in the company"], "default"),
            Question("Question 6: What is a cash flow statement used for?", ["A. To show the cash inflows and outflows from operating, investing, and financing activities", "B. To track customer transactions", "C. To manage inventory", "D. To calculate net income"], "default"),
            Question("Question 7: What are retained earnings?", ["A. The accumulated profits of a company that have not been distributed to shareholders", "B. The company's outstanding debt", "C. The company's stock price", "D. The company's net income"], "default"),
            Question("Question 8: What is the difference between accrual basis and cash basis accounting?", ["A. Accrual basis records transactions when they occur, while cash basis records transactions when cash is exchanged", "B. Accrual basis records transactions when cash is exchanged, while cash basis records transactions when they occur", "C. Accrual basis records transactions on a quarterly basis, while cash basis records transactions on a yearly basis", "D. Accrual basis records transactions on a yearly basis, while cash basis records transactions on a quarterly basis"], "default"),
            Question("Question 9: What is inventory valuation?", ["A. The method used to track customer transactions", "B. The method used to calculate revenue", "C. The method used to calculate net income", "D. The method used to assign a monetary value to inventory items"], "default"),
            Question("Question 10: What is the purpose of a balance sheet?", ["A. To provide a snapshot of a company's financial position at a specific point in time", "B. To track customer transactions", "C. To manage inventory", "D. To calculate revenue"], "default")
        ]

        #Populate for Marketing
        self.questions["Marketing"] = [
            Question("Question 1: What is marketing?", ["A. Selling products", "B. Creating and delivering value to customers", "C. Making profits", "D. Conducting surveys"], "default"),
            Question("Question 2: What is the marketing mix?", ["A. Product, price, place, promotion", "B. Product, price, place, policy", "C. Product, place, promotion, people", "D. Price, place, promotion, policy"], "default"),
            Question("Question 3: What is market segmentation?", ["A. Targeting specific markets with specialized products", "B. Marketing to a broad audience", "C. Adapting products for international markets", "D. Segmenting the market based on demographics, psychographics, or behavior"], "default"),
            Question("Question 4: What is a target market?", ["A. A market with high demand", "B. A market with low competition", "C. A specific group of consumers most likely to buy a product", "D. A group of potential investors"], "default"),
            Question("Question 5: What is a brand?", ["A. A logo", "B. A product", "C. A promise to customers", "D. A marketing campaign"], "default"),
            Question("Question 6: What is the difference between marketing and advertising?", ["A. Marketing is the process of promoting products or services, while advertising is just one component of marketing", "B. Marketing and advertising are the same thing", "C. Advertising is the process of creating products, while marketing is the process of selling them", "D. Marketing and advertising have no relation to each other"], "default"),
            Question("Question 7: What is a SWOT analysis?", ["A. An analysis of a company's strengths, weaknesses, opportunities, and threats", "B. An analysis of a company's sales performance", "C. An analysis of a company's financial statements", "D. An analysis of a company's customer demographics"], "default"),
            Question("Question 8: What is a marketing plan?", ["A. A document outlining a company's marketing objectives and strategies", "B. A document outlining a company's financial goals", "C. A document outlining a company's organizational structure", "D. A document outlining a company's product specifications"], "default"),
            Question("Question 9: What is the importance of market research?", ["A. To understand customer needs and preferences", "B. To fulfill legal requirements", "C. To increase production efficiency", "D. To reduce marketing costs"], "default"),
            Question("Question 10: What is customer relationship management (CRM)?", ["A. Managing interactions and relationships with customers", "B. Maximizing profits through advertising", "C. Developing new products", "D. Analyzing market trends"], "default")
        ]

        #Populate for Statistics
        self.questions["Statistics"] = [
            Question("Question 1: What is statistics?", ["A. The study of mathematics", "B. The study of data collection, organization, analysis, interpretation, and presentation", "C. The study of shapes", "D. The study of probability"], "default"),
            Question("Question 2: What is a population?", ["A. A small group of individuals selected from a larger group", "B. The entire group of individuals being studied", "C. A variable", "D. A constant"], "default"),
            Question("Question 3: What is a sample?", ["A. A small group of individuals selected from a larger group", "B. The entire group of individuals being studied", "C. A variable", "D. A constant"], "default"),
            Question("Question 4: What is the mean?", ["A. The most frequently occurring value in a dataset", "B. The middle value in a sorted dataset", "C. The average of all values in a dataset", "D. The range of values in a dataset"], "default"),
            Question("Question 5: What is the median?", ["A. The most frequently occurring value in a dataset", "B. The middle value in a sorted dataset", "C. The average of all values in a dataset", "D. The range of values in a dataset"], "default"),
            Question("Question 6: What is the mode?", ["A. The most frequently occurring value in a dataset", "B. The middle value in a sorted dataset", "C. The average of all values in a dataset", "D. The range of values in a dataset"], "default"),
            Question("Question 7: What is standard deviation?", ["A. A measure of the spread or dispersion of a dataset", "B. A measure of central tendency", "C. A measure of the relationship between two variables", "D. A measure of the variability of a dataset"], "default"),
            Question("Question 8: What is a normal distribution?", ["A. A distribution with a bell-shaped curve", "B. A distribution with a uniform shape", "C. A distribution with a skewed shape", "D. A distribution with no shape"], "default"),
            Question("Question 9: What is hypothesis testing?", ["A. A method used to estimate population parameters based on sample data", "B. A method used to compare two or more groups", "C. A method used to test the significance of a relationship between variables", "D. A method used to analyze categorical data"], "default"),
            Question("Question 10: What is correlation?", ["A. A measure of the strength and direction of the linear relationship between two variables", "B. A measure of the spread or dispersion of a dataset", "C. A measure of central tendency", "D. A measure of the variability of a dataset"], "default")
        ]

        #Populate for Business Applications
        self.questions["Business Applications"] = [
            Question("Question 1: What is a spreadsheet?", ["A. A type of accounting software", "B. A type of word processing software", "C. A software application used to create, manipulate, and analyze numerical data", "D. A type of presentation software"], "default"),
            Question("Question 2: What is a database?", ["A. A collection of related data organized for efficient retrieval", "B. A type of spreadsheet", "C. A type of word processing software", "D. A presentation software"], "default"),
            Question("Question 3: What is customer relationship management (CRM)?", ["A. A strategy for managing customer relationships and interactions", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 4: What is enterprise resource planning (ERP)?", ["A. A strategy for managing enterprise resources and operations", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 5: What is supply chain management (SCM)?", ["A. A strategy for managing the flow of goods and services from suppliers to customers", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 6: What is business intelligence (BI)?", ["A. A set of techniques and tools for transforming raw data into meaningful and useful information for business analysis", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 7: What is e-commerce?", ["A. Buying and selling goods and services over the internet", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 8: What is cloud computing?", ["A. A model of computing where resources are accessed via the internet rather than on local hardware", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 9: What is project management?", ["A. The practice of initiating, planning, executing, controlling, and closing the work of a team to achieve specific goals and meet specific success criteria", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default"),
            Question("Question 10: What is digital marketing?", ["A. The use of digital channels such as search engines, social media, email, and websites to connect with current and prospective customers", "B. A software application used to create, manipulate, and analyze numerical data", "C. A type of accounting software", "D. A type of word processing software"], "default")
        ]
    def create_category_selection(self):
        #Create category selection window
        self.category_window = tk.Toplevel(self.master)
        self.category_window.title("Select Category")
        
        #Widgets for the category selection
        tk.Label(self.category_window, text="Select Category:").pack()
        self.category_var = tk.StringVar(self.category_window)
        self.category_var.set("Accounting")  # Default category
        categories = ["Accounting", "Marketing", "Statistics", "Business Applications"]  # Example categories
        tk.OptionMenu(self.category_window, self.category_var, *categories).pack()
        
        tk.Button(self.category_window, text="Start Quiz Now", command=self.start_quiz).pack()

    def start_quiz(self):
        #Close category selection window
        self.category_window.destroy()
        
        #Quiz window
        self.quiz_window = tk.Toplevel(self.master)
        self.quiz_window.title("Quiz")

        #Get selected category
        selected_category = self.category_var.get()

        #Create canvas with scrollbar
        canvas = tk.Canvas(self.quiz_window)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.quiz_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        #Create frame for questions
        question_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=question_frame, anchor="nw")

        #Store the correct answers
        self.correct_answers = [question.answers[0] for question in self.questions[selected_category]]

        #Display the questions for the selected category
        self.answer_vars = []  # Store answer variables for each question
        for question in self.questions[selected_category]:
            question.display()
            tk.Label(question_frame, text=question.text).pack(anchor="w")

            #Create answer variables for each question
            answer_var = tk.StringVar(self.quiz_window)
            self.answer_vars.append(answer_var)

            for answer_choice in question.answers:
                answer_radio = tk.Radiobutton(question_frame, text=answer_choice, value=answer_choice, variable=answer_var)
                answer_radio.pack(anchor="w")

        #Scroll region 
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        #Button to submit answer
        submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.check_answer)
        submit_button.pack()

    def check_answer(self):
        #Get selected category
        selected_category = self.category_var.get()
        
        #Get user-selected answers
        user_answers = [answer_var.get() for answer_var in self.answer_vars]

        #Check user answers against correct answers
        correct_count = sum(1 for user_answer, correct_answer in zip(user_answers, self.correct_answers) if user_answer == correct_answer)
        
        #Calculate percentage correct
        percentage_correct = (correct_count / len(self.correct_answers)) * 100

        #Show user the feedback
        messagebox.showinfo("Result", f"You got {correct_count} out of {len(self.correct_answers)} correct. Percentage Correct: {percentage_correct:.2f}%")

def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()