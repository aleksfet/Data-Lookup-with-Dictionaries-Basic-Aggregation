# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Cybersecurity": 200,
    "IT Support": 100,
    "Data Analysis": 170,
    "Network Management": 175
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "EnhanceBuild Retail",
    "contact_person": "Alex Williams",
    "email": "alex@enhancebuildretail.com",
    "phone": "813-555-1001"
}

customer2 = {
    "company_name": "Dinero Finance Group",
    "contact_person": "James Hernando",
    "email": "james@dinerofinance.com",
    "phone": "813-555-1002"
}

customer3 = {
    "company_name": "Williams Legal Services",
    "contact_person": "Louis Campbell",
    "email": "louis@williamslegal.com",
    "phone": "813-555-1003"
}

customer4 = {
    "company_name": "RefinedPath Logistics",
    "contact_person": "Michael Scofield",
    "email": "michael@refinedpathlogistics.com",
    "phone": "813-555-1004"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for customer_id, customer_info in customers.items():
    print(f"{customer_id}: {customer_info['company_name']}")
    print(f"  Contact Person: {customer_info['contact_person']}")
    print(f"  Email: {customer_info['email']}")
    print(f"  Phone: {customer_info['phone']}")
    print()
    
# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("C002 info:", c002_info)
print("C003 contact:", c003_contact)
print("C999 lookup:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = "813-555-9001"
customers["C002"]["industry"] = "Finance"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
project1 = {
    "name": "Website Redesign",
    "service": "Web Development",
    "hours": 100,
    "budget": 15000
}

project2 = {
    "name": "Sales Data Dashboard",
    "service": "Data Analysis",
    "hours": 60,
    "budget": 10200
}

project3 = {
    "name": "Security System Upgrade",
    "service": "Cybersecurity",
    "hours": 70,
    "budget": 14000
}

project4 = {
    "name": "Office Tech Support Setup",
    "service": "IT Support",
    "hours": 50,
    "budget": 5000
}

project5 = {
    "name": "Network Infrastructure Update",
    "service": "Network Management",
    "hours": 80,
    "budget": 14000
}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

print("\nProject Information:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    print(f"{customer_id} Projects:")
    for project in project_list:
        print(project)
    print()

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    for project in project_list:
        hourly_rate = services[project["service"]]
        cost = hourly_rate * project["hours"]
        print(f"{project['name']} cost: ${cost}")

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
customer_ids = list(customers.keys())
customer_companies = [customer["company_name"] for customer in customers.values()]
total_customers = len(customers)

print("Customer IDs:", customer_ids)
print("Companies:", customer_companies)
print("Total customers:", total_customers)

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service_name = project["service"]
        service_counts[service_name] = service_counts.get(service_name, 0) + 1

for service, count in service_counts.items():
    print(f"{service}: {count}")

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
hours_list = []
budget_list = []

for project_list in projects.values():
    for project in project_list:
        hours_list.append(project["hours"])
        budget_list.append(project["budget"])

total_hours = sum(hours_list)
total_budget = sum(budget_list)
avg_budget = total_budget / len(budget_list)
max_budget = max(budget_list)
min_budget = min(budget_list)

print("Total hours:", total_hours)
print("Total budget:", total_budget)
print("Average budget:", avg_budget)
print("Max budget:", max_budget)
print("Min budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer_id, customer_info in customers.items():
    project_list = projects.get(customer_id, [])
    total_customer_hours = sum(project["hours"] for project in project_list)
    total_customer_budget = sum(project["budget"] for project in project_list)

    print(customer_id, customer_info["company_name"])
    print("Projects:", len(project_list))
    print("Total hours:", total_customer_hours)
    print("Total budget:", total_customer_budget)
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:.2f}")

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {
    customer_id: customer_info
    for customer_id, customer_info in customers.items()
    if customer_id in projects
}
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {
    customer_id: sum(project["budget"] for project in project_list)
    for customer_id, project_list in projects.items()
}
for customer_id, budget in customer_budgets.items():
    print(f"{customer_id}: ${budget}")

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]

    for field in required_fields:
        if field not in customer_dict:
            return False
    return True
print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
for customer_id, customer_info in customers.items():
    print(customer_id, validate_customer(customer_info))
    
# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
status_list = ["active", "completed", "pending", "active", "completed"]
status_counts = {}
index = 0

for project_list in projects.values():
    for project in project_list:
        project["status"] = status_list[index]
        index += 1

        status = project["status"]
        status_counts[status] = status_counts.get(status, 0) + 1

print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
def analyze_customer_budgets(projects_dict):
    results = {}

    for customer_id, project_list in projects_dict.items():
        total = sum(project["budget"] for project in project_list)
        count = len(project_list)

        if count > 0:
            average = total / count
        else:
            average = 0

        results[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results
print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
analysis = analyze_customer_budgets(projects)
print(analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
def recommend_services(customer_id, customers, projects, services):
    used_services = []

    for project in projects.get(customer_id, []):
        used_services.append(project["service"])

    recommendations = []

    for service in services:
        if service not in used_services:
            recommendations.append(service)

    return recommendations
print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
for customer_id in customers:
    recommendations = recommend_services(customer_id, customers, projects, services)
    print(customer_id, "recommended:", recommendations)