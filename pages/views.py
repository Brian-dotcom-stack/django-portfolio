from django.shortcuts import render

def home(request):
    # Define your skills data here
    skills = [
        {
            'name': 'Cloud Computing',
            'icon': 'aws',  # Adjust based on your actual SVG icon filename (without .svg)
            'percentage': 80,
            'color': 'bg-success',  # Bootstrap class for progress bar color
            'description': 'Proficient in designing, deploying, and managing cloud-based infrastructure across major platforms such as AWS, GCP, and Azure.',
        },
        {
            'name': 'DevOps',
            'icon': 'devops',
            'percentage': 70,
            'color': 'bg-info',
            'description': 'Experience with CI/CD, Docker, Kubernetes, and automation tools.',
        },
        {
            'name': 'Machine Learning',
            'icon': 'ml',
            'percentage': 75,
            'color': 'bg-warning',
            'description': 'Skilled in developing ML models and algorithms, utilizing frameworks like TensorFlow and scikit-learn.',
        },
        # Add more skills as needed
    ]
    
    # Pass the skills data to the template
    return render(request, "pages/home.html", {'skills': skills})
