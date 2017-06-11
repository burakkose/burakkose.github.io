def print_job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result, slot = [None] * len(jobs), [False] * len(jobs)
    for job in jobs:
        j = min(len(jobs), job[1]) - 1
        while j >= 0:
            if not slot[j]:
                result[j] = job[0]
                slot[j] = True
                break
            j -= 1

    print(result, sep='\n')

if __name__ == '__main__':
    # (id,zaman aşımı,kazanç)
    jobs = [('a', 2, 100), ('b', 1, 19),
            ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    print_job_scheduling(jobs)
