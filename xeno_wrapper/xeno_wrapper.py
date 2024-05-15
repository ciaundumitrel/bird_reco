from xenopy import Query

# birds = ["Common Buzzard", "Mallard", "Mute Swan", "Great Tit", "Red-backed Strike", "Hooded Crow",
#          "Rock Pigeon", "Eurasic Blackbird", "Eurasic Kestrel", "Grey Heron", "Common Chaffinch",
#          "Black-headed Gull", "Great Cormorant", "White Wagtail", "European Starling", "Eurasian Coot",
#          "White Stork", "House Sparrow", "Great Egret", "Eurasian Jay", "Eurasian Magpie", "Rook",
#          "Western Marsh Harrier", "Fieldfare", "Commmon Raven", "Eurasian Tree Sparrow"]

# birds = ["House Sparrow"]
# "Rock Pigeon", "Eurasic Blackbird", "Eurasic Kestrel", "Grey Heron", "Common Chaffinch",
# "Black-headed Gull", "Great Cormorant", "White Wagtail", "European Starling", "Eurasian Coot",
# "White Stork", "House Sparrow", "Great Egret", "Eurasian Jay", "Eurasian Magpie", "Rook",
# "Western Marsh Harrier", "Fieldfare", "Commmon Raven", "Eurasian Tree Sparrow"]
from utils import birds


def download_sounds():
    for bird_name in birds:
        q = Query(name=bird_name, q_gt="A", since="2022-01-01")
        metafiles = q.retrieve_meta(verbose=True)
        # print(metafiles['recordings'])
        q.retrieve_recordings(multiprocess=True, nproc=5, attempts=1, outdir=f"../sounds/{bird_name}")


if __name__ == "__main__":
    pass
