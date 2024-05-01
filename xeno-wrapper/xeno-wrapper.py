from xenopy import Query

if __name__ == "__main__":
    q = Query(name="Greylag Goose", q_gt="C", since="2022-01-01")

    metafiles = q.retrieve_meta(verbose=True)
    q.retrieve_recordings(multiprocess=True, nproc=5, attempts=1, outdir="datasets/")
