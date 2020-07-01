import csv
import glob



citation = input("Input the citation minus Bibtex formatting, i.e. author_title_year: ")


for file in glob.glob('./input/*.csv'):
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='"')
        for num in range(0,8):
            next(data)
        with open(f'output/{citation}.md', 'w') as output_file:
            for row in data:
                page_num = row[1].split()[1]
                cit_num = f"[@{citation} {page_num}]"
                quotation_text = row[3]
                cited_quotation = f">'{quotation_text}' {cit_num}\n\n"
                output_file.write(cited_quotation)
                print("Cited quotation prepared.")

print("Quotation preparations completed.")


