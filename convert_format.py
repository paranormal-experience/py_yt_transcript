def calculate_and_format_times(start_time, duration):
    # Convert start time and duration to seconds
    start_seconds = float(start_time)
    duration_seconds = float(duration)
    
    # Calculate end time in seconds
    end_seconds = start_seconds + duration_seconds
    
    # Calculate hours, minutes, and seconds for start time
    start_hours = int(start_seconds // 3600)
    start_minutes = int((start_seconds % 3600) // 60)
    start_seconds = start_seconds % 60
    
    # Calculate hours, minutes, and seconds for end time
    end_hours = int(end_seconds // 3600)
    end_minutes = int((end_seconds % 3600) // 60)
    end_seconds = end_seconds % 60
    
    # Format the times into the desired subtitle format
    formatted_start_time = f"{start_hours:02d}:{start_minutes:02d}:{start_seconds:.3f}"
    formatted_end_time = f"{end_hours:02d}:{end_minutes:02d}:{end_seconds:.3f}"
    
    # Combine the formatted times into the subtitle format
    formatted_subtitle = f"{formatted_start_time.replace('.', ',')} --> {formatted_end_time.replace('.', ',')}"
    
    return formatted_subtitle

# # Example usage
# start_time = "17.66"  # Example start time in seconds
# duration = "10.789"   # Example duration in seconds
# formatted_subtitle = calculate_and_format_times(start_time, duration)
# print(formatted_subtitle)
# # 30.68 --> 3.23

# start_time = "30.68"  # Example start time in seconds
# duration = "3.23"   # Example duration in seconds
# formatted_subtitle = calculate_and_format_times(start_time, duration)
# print(formatted_subtitle)