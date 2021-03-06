import unittest
from classes import downloader
from scripts import setup

class TestDownloaderFunctions(unittest.TestCase):

    def __prep(self):
        setup.prep_env_from_file('credentials.txt')
        self.user_id = 'swagnacy'
        self.downloader = downloader.Downloader(self.user_id)
        

    def test_downloader_instantiation(self):
        self.__prep()

        self.assertIsNotNone(self.downloader.spotify, "Spotify client not initialized")


    def test_fetch_single_track_by_name(self):
        self.__prep()

        track = self.downloader.fetch_single_track_by_name('Sonne')
        self.assertIsNotNone(track, 'Track failed to download.')

    def test_fetch_all_user_playlists(self):
        self.__prep()

        playlists = self.downloader.fetch_all_user_playlists()

        self.assertIsNotNone(playlists, 'Playlists failed to download.')
        self.assertTrue(len(playlists.items()) > 0, 'Playlists failed to download.')

    def test_write_read_json(self):
        self.__prep()

        dic = {}
        self.downloader.write_json_to_file('test.json', dic)
        res = self.downloader.read_json_from_file('test.json')

        self.assertEqual(dic, res, 'Failed to write/read json.')

