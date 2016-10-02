__author__ = 'Bamba'


import CJSaveus as jc


def aggr_extractor():
    metafields, values = jc.load_from_csv_file()


    for filename, sample in jc.load_every_mat_in_dir():
        s = {}
        avgpos = {k: [0 for x in range(0, 3)] for k in sample}
        avgspd = {k: [0 for x in range(0, 3)] for k in sample}

        for joint in sample:
            for i in range(0, len(sample[joint])):
                for j in range(0, 3):
                    avgpos[joint][j] += sample[joint][i][j]
            avgpos[joint] = [avgpos[joint][j] / len(sample[joint]) for j in range(0, 3)]

        for joint in sample:
            for i in range(1, len(sample[joint])):
                for j in range(0, 3):
                    avgspd[joint][j] += sample[joint][i][j] - sample[joint][i-1][j]
            avgspd[joint] = [avgspd[joint][j] / len(sample[joint]) for j in range(0, 3)]

        for v in values:
            if v["motion_id"] == filename:
                s["class"] = v["modal_category"]

        #add data to dict
        s["avgspd"] = avgspd
        s["avgpos"] = avgpos
        yield(s)


#===================================================================
a = []
for d in aggr_extractor():
    a.append(d)
    print(".")

with open("culomille.txt", "a+") as file:
    for el in a:
        file.write(str(el) + "\n")
