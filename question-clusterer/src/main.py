from clustering import cluster_questions

if __name__ == "__main__":
    # Read questions from text file
    with open("../questions.txt", "r", encoding="utf-8") as f:
        questions = [line.strip() for line in f if line.strip()]
    
    clusters = cluster_questions(questions)

    print(f"📊 Found {len(clusters)} clusters:\n")
    for i, cluster in enumerate(clusters, 1):
        print(f"🏷️ CLUSTER {i} (Size: {cluster['size']})")
        print(f"🔹 Main Theme: {cluster['theme']}")
        print(f"⭐ Representative Question: {cluster['representative']}")
        print("\n📋 All Questions in This Cluster:")
        for q in cluster['all_questions']:
            print(f"  - {q}")
        print("\n" + "="*80 + "\n")
