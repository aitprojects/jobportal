from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import sys
#import wikipedia
import csv

pure_tags = [
    "fintech",
    "iot",
    "finance",
    "internet of things",
    "data & analytics",
    "e-commerce",
    "software",
    "consulting",
    "consumer",
    "analytics",
    "hardware",
    "internet software",
    "health care",
    "banking & accounting",
    "health/medical",
    "education",
    "b2b/enterprise",
    "home",
    "advertising",
    "technology",
    "financial services",
    "information technology",
    "marketing",
    "enterprise software",
    "automotive",
    "web development",
    "it services",
    "healthcare",
    "manufacturing",
    "big data",
    "solutions",
    "insurance",
    "healthcare it",
    "services",
    "agriculture",
    "energy & cleantech",
    "security",
    "platform",
    "saas",
    "business support services",
    "cloud computing",
    "artificial intelligence",
    "technologies",
    "mobile application",
    "cloud",
    "machine learning",
    "big data analytics",
    "web design",
    "application software",
    "android",
    "customers",
    "smart cities",
    "enterprises",
    "fashion",
    "development",
    "business",
    "transportation",
    "businesses",
    "robotics",
    "payments",
    "computer security",
    "social media",
    "predictive analytics",
    "hospitals",
    "entertainment",
    "automation",
    "media",
    "real estate",
    "ios",
    "consumer electronics",
    "ecommerce",
    "logistics/supply chain",
    "digital media",
    "electronics",
    "information",
    "Financial Services",
    "marketplace",
    "social enterprise",
    "mobile payments",
    "health care services",
    "Internet Software",
    "digital marketing",
    "logistics",
    "industrial",
    "accounting",
    "seo",
    "industrial automation",
    "service",
    "online platform",
    "systems software",
    "computer networking",
    "software development",
    "website",
    "home automation",
    "mobile commerce",
    "health",
    "startups",
    "money",
    "mobile apps",
    "fitness",
    "lifestyle",
    "architecture & construction",
    "system",
    "Business Support Services",
    "industries",
    "banking",
    "telecommunications",
    "mobile app",
    "health and wellness",
    "healthcare services",
    "mobile health",
    "FinTech",
    "medical devices",
    "sensors",
    "diversified financial services",
    "wearables",
    "cyber security",
    "application",
    "management",
    "Machine Learning",
    "Artificial Intelligence",
    "IT Services",
    "information services",
    "biotechnology",
    "Software",
    "online shopping",
    "social media marketing",
    "data analytics",
    "product development",
    "personal health",
    "outsourcing",
    "e-commerce platforms",
    "Analytics",
    "retailers",
    "Diversified Financial Services",
    "retail technology",
    "product design",
    "smartphone",
    "legal services",
    "E-Commerce",
    "healthtech",
    "biotech",
    "personal loan",
    "bitcoin",
    "personal finance",
    "management consulting services",
    "3d printing",
    "construction",
    "business loan"
]

'''
def prepare_csv_file():
    csvfile = open('dataset.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['tag', 'context'])
    for i in pure_tags:
        try:
            search = wikipedia.search(i)
            ny = wikipedia.page(search[0])
            print('Saving article for: ' + i + '...')
            writer.writerow([i, ny.summary])
        except:
            continue
    csvfile.close()


'''

def get_tfidf_matrix(dataset):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset)
    return tfidf_matrix

def get_closest_neighs(word, tfidf_matrix):
    nbrs = NearestNeighbors(n_neighbors=10).fit(tfidf_matrix)
    row = dataset.index.get_loc(word)
    distances, indices = nbrs.kneighbors(tfidf_matrix.getrow(row))
    names_similar = pd.Series(indices.flatten()).map(dataset.reset_index()['tag'])
    result = pd.DataFrame({'distance':distances.flatten(), 'name':names_similar})
    return result

if __name__ == '__main__':
    #prepare_csv_file()
    dataset = pd.read_csv('dataset.csv', index_col='tag')['context']
    tfidf_matrix = get_tfidf_matrix(dataset)
    print(get_closest_neighs('Analytics'.lower(), tfidf_matrix))