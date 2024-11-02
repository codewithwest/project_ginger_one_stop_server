
youtube_downloader_types = """
    type downloadLink {
        download_link: String!
        }
    """


youtube_downloader_queries =  """
    type Query {
        getDownloadLink(link: String!): [downloadLink]
    }
    """


youtube_downloader_mutations =  """ """

