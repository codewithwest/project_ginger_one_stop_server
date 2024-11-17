
youtube_downloader_types = """
    type availableFormats {
        ext: String,
        url: String,
        resolution: String,
        width: Int,
        height: Int,
        video_extension: String,
        audio_extension: String,
        filesize_approx: Int,
        filesize: Int, 
        manifest_url: String,
        format: String,
    }
  
    type videoDownloadResponse {
            title: String,
            video_duration: Int,
            ext: String,
            filesize_approx: Int,
            highest_width: Int,
            highest_height: Int,
            highest_resolution: String,
            webpage_url: String,
            formats:[availableFormats],
        }
    
    """
youtube_downloader_queries =  """
        getYouTubeVideoDownloadData(link: String!): [videoDownloadResponse]
    """

youtube_downloader_mutations =   """ """

