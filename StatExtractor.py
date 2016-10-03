__author__ = 'Bamba'


import CJSaveus as jc
import os


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

        #find ref in csv
        ref_csv = None
        for v in values:
            if v["motion_id"] == filename:
                ref_csv = v

        #add values to dict
        s["id"] = filename
        s["class"] = ref_csv["modal_category"]
        s["avgspd"] = avgspd
        s["avgpos"] = avgpos
        yield(s)


def save(l):
    with open("culomille.txt", "w+") as file:
        for el in l:
            file.write(str(el) + "\n")


#===================================================================
#===================================================================
#===================================================================


save(aggr_extractor())