def sol(companies, applicants):
    companies_info = dict()
    applicants_info = dict()
    candidate = dict()

    for company in companies:
        tmp = company.split(' ')
        companies_info[tmp[0]] = [tmp[1], int(tmp[2])]

    for applicant in applicants:
        tmp = applicant.split(' ')
        applicants_info[tmp[0]] = [tmp[1], int(tmp[2]), 0, True]

    while True:

        flag = False
        for applicant in applicants_info.keys():

            if applicants_info[applicant][3] and applicants_info[applicant][1] > applicants_info[applicant][2]:

                candidate_company = applicants_info[applicant][0][applicants_info[applicant][2]]

                if candidate_company in candidate.keys():
                    candidate[candidate_company].append(applicant)
                else:
                    candidate[candidate_company] = [applicant]

                applicants_info[applicant][3] = False
                applicants_info[applicant][2] += 1
                flag = True

        for company, candidate_applicants in candidate.items():

            cnt = 0
            tmp = set()
            for preference in companies_info[company][0]:

                if companies_info[company][1] > cnt:
                    for candidate_applicant in candidate_applicants:
                        if candidate_applicant == preference:
                            cnt += 1
                            tmp.add(candidate_applicant)
                            break
                else:
                    break

            for candidate_applicant2 in candidate_applicants:
                if candidate_applicant2 not in tmp:
                    applicants_info[candidate_applicant2][3] = True

            candidate[company] = list(tmp)

        if not flag:
            break

    ret = []
    for company in companies_info.keys():
        if company in candidate.keys():
            ret.append(company+"_"+ ''.join(sorted(candidate[company])))
        else:
            ret.append(company+"_")

    ret.sort(key=lambda x:x[0])
    return ret

sol(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"])
sol(["A abc 2", "B abc 1"], ["a AB 1", "b AB 1","c AB 1"])
