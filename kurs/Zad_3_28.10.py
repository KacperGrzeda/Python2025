subjects = ['język polski', 'matematyka', 'religia']
newsubjects = ['angielski', 'przyroda']
subjects.append(newsubjects)
subjects.remove('język polski')
subjects.append('język indonezyjski')
subjects.remove('religia')
subjects.clear()
print(subjects)
print(len(subjects))