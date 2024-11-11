
youtube_downloader_types = """
    type availableFormats {
        ext: String,
        url: String,
        resolution: String,
        width: String,
        height: String,
        video_extension: String,
        audio_extension: String,
        filesize_approx: String,
        filesize: String, 
        manifest_url: String,
        format: String,
    }
  
    type videoDownloadResponse {
            title: String,
            video_duration: String,
            ext: String,
            filesize_approx: String,
            highest_width: String,
            highest_height: String,
            highest_resolution: String,
            webpage_url: String,
            formats:[availableFormats],
        }
    
    """
youtube_downloader_queries =  """
    type Query {
        getYouTubeVideoDownloadData(link: String!): [videoDownloadResponse]
    }
    """


youtube_downloader_mutations =   """ """

